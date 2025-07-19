import os
import hashlib
import pandas as pd

from docx import Document
from mimetypes import guess_extension
from langchain.docstore.document import Document as LCDocument
from docx.oxml.text.paragraph import CT_P
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.table import Table
from pybloom_live import BloomFilter
from pathlib import Path

from config import config

class DocxHandler:
    @classmethod
    def load_docx_file(cls, file_path):
        cat, fil = Path(file_path).parts[-2:]

        imgs_dir = str(os.path.join(config.IMGS_ROOT_OS, cat, fil))

        document = Document(file_path)

        texts = list()

        for block in document.element.body:
            if isinstance(block, CT_P):
                paragraph = Paragraph(block, document)

                if paragraph._element.xpath(".//w:drawing"):
                    texts += cls.__proc_drawing(paragraph, document, imgs_dir, cat, fil)
                    continue

                if paragraph.text.strip():
                    texts.append(paragraph.text)
                    continue

                continue

            if isinstance(block, CT_Tbl):
                table = Table(block, document)

                text = cls.__proc_tbl(table)
                texts.append(text)

                continue

        full_text = "\n".join(texts)

        return [LCDocument(page_content=full_text)]

    @classmethod
    def __proc_drawing(cls, paragraph, document, imgs_dir, cat, fil):
        texts = list()

        bloom_filter = BloomFilter(capacity=100000, error_rate=0.001)

        for run in paragraph.runs:
            drawing_elements = run._element.xpath(".//a:blip")

            for blip in drawing_elements:
                r_id = blip.attrib.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                )

                img_part = document.part.related_parts[r_id]
                img_bytes = img_part.blob
                img_hash = cls.__get_hash(bloom_filter, img_bytes)
                img_ext = guess_extension(img_part.content_type) or ".png"
                img_name = f"{img_hash}{img_ext}"
                img_path = os.path.join(imgs_dir, img_name)

                with open(img_path, "wb") as file:
                    file.write(img_bytes)

                img_url = f"http://{config.HOST}:{config.PORT}{config.IMG_PREFIX}/{cat}/{fil}/{img_name}"

                texts.append(f"![image]({img_url})")

        return texts

    @staticmethod
    def __proc_tbl(table):
        rows = list()

        for row in table.rows:
            cells = [cell.text.strip().replace("\n", "") for cell in row.cells]
            rows.append(cells)

        if not rows:
            return ""

        max_len = max(len(row) for row in rows)
        normalized_data = [row + [""] * (max_len - len(row)) for row in rows]

        data_frame = pd.DataFrame(
            normalized_data[1:],columns=normalized_data[0]
        ) if len(normalized_data) > 1 else pd.DataFrame(normalized_data)

        return data_frame.to_markdown(index=False)

    @staticmethod
    def __get_hash(bloom_filter, img_bytes):
        img_hash = hashlib.md5(img_bytes).hexdigest()[:6]

        while img_hash in bloom_filter:
            img_hash = hashlib.md5(
                (img_hash + config.BF_SALT).encode()
            ).hexdigest()[:6]

        bloom_filter.add(img_hash)

        return img_hash

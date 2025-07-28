import os
import pandas as pd

from docx import Document
from mimetypes import guess_extension
from langchain.docstore.document import Document as LCDocument
from docx.oxml.text.paragraph import CT_P
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.table import Table
from pathlib import Path

from config import config
from rag.hashhandler import hash_handler

class DocxHandler:
    @classmethod
    def load_docx_file(cls, file_path):
        cat, fil = Path(file_path).parts[-2:]

        cat = hash_handler.gen_hash_name(cat)
        fil = hash_handler.gen_hash_name(fil)

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

        for run in paragraph.runs:
            drawing_elements = run._element.xpath(".//a:blip")

            for blip in drawing_elements:
                r_id = blip.attrib.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                )

                img_part = document.part.related_parts[r_id]
                img_bytes = img_part.blob
                img_hash = hash_handler.gen_img_hash_name(img_bytes)
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

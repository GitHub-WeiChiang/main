from enum import Enum, unique, auto


@unique
class CommandEnum(Enum):
    # ============================================================
    # --------------------------- Open ---------------------------
    # ============================================================

    OPEN_PORT = auto(),
    OPEN_PORT_SECURITY = auto(),
    OPEN_PORT_SECURITY_STICKY = auto(),
    OPEN_PORT_SECURITY_STATIC = auto(),
    OPEN_SNMP_SERVER = auto(),

    # ============================================================
    # -------------------------- Close ---------------------------
    # ============================================================

    CLOSE_PORT = auto(),
    CLOSE_PORT_SECURITY = auto(),
    CLOSE_PORT_SECURITY_STICKY = auto(),
    CLOSE_PORT_SECURITY_STATIC = auto(),
    CLOSE_SNMP_SERVER = auto(),

    # ============================================================
    # -------------------------- Create --------------------------
    # ============================================================

    CREATE_VLAN = auto(),
    CREATE_POLICE = auto(),
    CREATE_ACL_PERMIT = auto(),
    CREATE_ACL_DENY = auto(),
    CREATE_EXT_ACL_PERMIT = auto(),
    CREATE_EXT_ACL_DENY = auto(),

    # ============================================================
    # --------------------------- Set ----------------------------
    # ============================================================

    SET_SPEED = auto(),
    SET_DUPLEX = auto(),
    SET_VLAN = auto(),
    SET_POLICE_IN = auto(),
    SET_POLICE_OUT = auto(),
    SET_ACL_IN = auto(),
    SET_ACL_OUT = auto(),
    SET_PORT_SECURITY_MAXIMUM = auto(),
    SET_PORT_SECURITY_VIO_PROTECT = auto(),
    SET_PORT_SECURITY_VIO_RESTRICT = auto(),
    SET_PORT_SECURITY_VIO_SHUTDOWN = auto(),
    SET_INTERFACE_DESCRIPTION = auto(),

    # ============================================================
    # -------------------------- Unset ---------------------------
    # ============================================================

    UNSET_POLICE_IN = auto(),
    UNSET_POLICE_OUT = auto(),

    # ============================================================
    # -------------------------- Clear ---------------------------
    # ============================================================

    CLEAR_PORT_SECURITY_ALL = auto(),
    CLEAR_POLICE = auto(),

    # ============================================================
    # --------------------------- Show ---------------------------
    # ============================================================

    SHOW_PMAP_LIST = auto(),
    SHOW_PMAP_INT_LIST = auto(),
    SHOW_RUNNING_CONFIG = auto(),
    SHOW_PORT_SECURITY_ADDRESS = auto(),
    SHOW_SNMP_HOST = auto(),

    # ============================================================
    # -------------------------- Other ---------------------------
    # ============================================================

    CUSTOM = auto(),

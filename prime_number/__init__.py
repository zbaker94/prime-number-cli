__appname__ = "prime_number_cli"
__version__ = "0.1.0"

(
    SUCCESS,
    ARG_ERROR,
    DIR_READ_ERROR, 
    FILE_READ_ERROR,
    DIR_CREATE_ERROR,
    FILE_WRITE_ERROR,
    PARSE_ERROR,
) = range(7)

ERRORS = {
    SUCCESS: "Success",
    ARG_ERROR: "Argument Error",
    DIR_READ_ERROR: "Cache Directory not found",
    FILE_READ_ERROR: "File not found",
    DIR_CREATE_ERROR: "Cache Directory not created",
    FILE_WRITE_ERROR: "File not written",
    PARSE_ERROR: "Error parsing cache file",
}
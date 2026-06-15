# SQL Datatypes

| Datatype        | Description                             |
| --------------- | --------------------------------------- |
| `INT`           | Integer values                          |
| `BIGINT`        | Large integer values                    |
| `FLOAT`         | Floating-point numbers                  |
| `DOUBLE`        | Double-precision floating-point numbers |
| `DECIMAL(p, s)` | Fixed-precision decimal numbers         |
| `CHAR(n)`       | Fixed-length string                     |
| `VARCHAR(n)`    | Variable-length string                  |
| `TEXT`          | Large text data                         |
| `DATE`          | Date values (`YYYY-MM-DD`)              |
| `TIME`          | Time values (`HH:MM:SS`)                |
| `DATETIME`      | Date and time values                    |
| `TIMESTAMP`     | Timestamp values                        |
| `BOOLEAN`       | Boolean values (`TRUE` or `FALSE`)      |
| `BLOB`          | Binary large object data                |
| `BIT`           | Store value in bits                     |

---
# Detailed Sizes and Data-Types

| Datatype           | Description                            | Storage Size                      |
| ------------------ | -------------------------------------- | --------------------------------- |
| `TINYINT`          | Very small integer                     | 1 byte                            |
| `SMALLINT`         | Small integer                          | 2 bytes                           |
| `MEDIUMINT`        | Medium-sized integer                   | 3 bytes                           |
| `INT` / `INTEGER`  | Standard integer                       | 4 bytes                           |
| `BIGINT`           | Large integer                          | 8 bytes                           |
| `FLOAT`            | Single-precision floating-point number | 4 bytes                           |
| `DOUBLE`           | Double-precision floating-point number | 8 bytes                           |
| `DECIMAL(p, s)`    | Fixed-precision decimal number         | Variable                          |
| `CHAR(n)`          | Fixed-length string                    | `n` bytes                         |
| `VARCHAR(n)`       | Variable-length string                 | `n + 1/2` bytes                   |
| `TINYTEXT`         | Small text data                        | Up to 255 bytes                   |
| `TEXT`             | Text data                              | Up to 65,535 bytes (~64 KB)       |
| `MEDIUMTEXT`       | Medium-sized text data                 | Up to 16,777,215 bytes (~16 MB)   |
| `LONGTEXT`         | Large text data                        | Up to 4,294,967,295 bytes (~4 GB) |
| `TINYBLOB`         | Small binary object                    | Up to 255 bytes                   |
| `BLOB`             | Binary large object                    | Up to 65,535 bytes (~64 KB)       |
| `MEDIUMBLOB`       | Medium-sized binary object             | Up to 16,777,215 bytes (~16 MB)   |
| `LONGBLOB`         | Large binary object                    | Up to 4,294,967,295 bytes (~4 GB) |
| `DATE`             | Date value (`YYYY-MM-DD`)              | 3 bytes                           |
| `TIME`             | Time value (`HH:MM:SS`)                | 3 bytes                           |
| `DATETIME`         | Date and time value                    | 8 bytes                           |
| `TIMESTAMP`        | Timestamp value                        | 4 bytes                           |
| `YEAR`             | Year value                             | 1 byte                            |
| `BOOLEAN` / `BOOL` | Boolean value (`TRUE` or `FALSE`)      | 1 byte                            |
| `ENUM`             | One value from a predefined list       | 1 or 2 bytes                      |
| `SET`              | Multiple values from a predefined list | 1, 2, 3, 4, or 8 bytes            |
| `BIT`              | Store value in bits                    | BIT(n), n up to 64                |

---

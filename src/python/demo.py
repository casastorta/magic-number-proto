#!/usr/bin/env python3.10

from typing import Callable, Tuple
import os

"""
MagicNumber data type, to contain all magic numbers for magic logic ;-)
"""
MagicNumber = Tuple[Tuple[int, bytes], ...]

"""
CheckFunction data type, signature for the all format checks interface methods
"""
CheckFunction = Callable[[bytes], bool]

"""
Maximum payload size to load for detection.
Change this constant if you need bigger chunk of bytes to work with more complex magic numbers
"""
MAX_PAYLOAD_SIZE: int = 40


def main():
    script_path: str = os.path.realpath(__file__)
    test_base_path: str = os.path.realpath(
        "%s/../../../tests/resources" % (script_path,)
    )
    testcases = (
        ("%s/empty_file.bin" % test_base_path),
        ("%s/jfif_jpeg.jpeg" % test_base_path),
        ("%s/olympus-c960.jpg" % test_base_path),
        ("%s/PNG_transparency_demonstration_1.png" % test_base_path),
        ("%s/sample.pdf" % test_base_path),
        ("%s/small_archive.zip" % test_base_path),
        ("%s/small_file.txt" % test_base_path),
    )

    detector: MagicNumberDetection = MagicNumberDetection()

    for testcase in testcases:  # type: str
        with open(testcase, "rb") as fp:
            payload = fp.read(MAX_PAYLOAD_SIZE)
            print("%s %s header is: %s" % (testcase, os.linesep, payload))

            print(
                " -> %s is some of the image formats: %s"
                % (testcase, detector.check_image(payload))
            )
            print(" `-> %s is JPEG: %s" % (testcase, detector.check_jpeg(payload)))
            print(" `-> %s is JPEG2k: %s" % (testcase, detector.check_jpeg2k(payload)))
            print(" `-> %s is PNG: %s" % (testcase, detector.check_png(payload)))

            print()

            print(" -> %s PDF: %s" % (testcase, detector.check_pdf(payload)))

            print()

            print(
                " -> %s is some of the archive formats: %s"
                % (testcase, detector.check_archive(payload))
            )
            print(" `-> %s is (PK)ZIP: %s" % (testcase, detector.check_zip(payload)))
            print(" `-> %s is GZIP: %s" % (testcase, detector.check_gzip(payload)))
            print(" `-> %s is XZ: %s" % (testcase, detector.check_xz(payload)))

            print("-" * 70)


class MagicNumberDetection:
    """
    Logic for detecting formats utilizing magic numbers
    """

    class FileTypes:
        """
        File types magic numbers constants in format
        Tuple(offset, values[, offset, values[, offset, values....]])

        Offset is measure of bytes from the beginning of the file.

        Implemented filetypes are based on the list from https://en.wikipedia.org/wiki/List_of_file_signatures

        Known unsupported use-cases:
        - Filetypes with flexible/repeatable offsets (containers formats like Amiga IFF)
        - Filetypes with repeating offset (for example MPEG-2)
        - Filetypes with negative offset relative to the end of file (for example Apple Disk Image)
        """

        # Image formats
        IMAGE_JPEG: MagicNumber = (
            (0, b"\xFF\xD8\xFF\xDB"),
            (0, b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01"),
            (0, b"\xFF\xD8\xFF\xEE"),
            (0, b"\xFF\xD8\xFF\xE1", 6, b"\x45\x78\x69\x66\x00\x00"),
        )
        IMAGE_JPEG2K: MagicNumber = (
            (0, b"\x00\x00\x00\x0C\x6A\x50\x20\x20\x0D\x0A\x87\x0A"),
            (0, b"\xFF\x4F\xFF\x51"),
        )
        IMAGE_PNG: MagicNumber = ((0, b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"),)

        # Document formats
        DOCUMENT_PDF: MagicNumber = ((0, b"\x25\x50\x44\x46\x2D"),)

        # Archive formats
        ARCHIVE_GZIP: MagicNumber = ((0, b"\x1F\x8B"),)
        ARCHIVE_XZ: MagicNumber = ((0, b"\xFD\x37\x7A\x58\x5A\x00"),)
        ARCHIVE_PKZIP: MagicNumber = (
            (0, b"\x50\x4B\x03\x04"),
            (0, b"\x50\x4B\x05\x06"),
            (0, b"\x50\x4B\x07\x08"),
        )

    def check_image(self, payload: bytes) -> bool:
        checks: Tuple[CheckFunction, ...] = (
            self.check_jpeg,
            self.check_jpeg2k,
            self.check_png,
        )
        return self.check_multiple_or(payload, checks)

    def check_jpeg(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.IMAGE_JPEG)

    def check_jpeg2k(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.IMAGE_JPEG2K)

    def check_png(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.IMAGE_PNG)

    def check_pdf(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.DOCUMENT_PDF)

    def check_archive(self, payload: bytes) -> bool:
        checks: Tuple[CheckFunction, ...] = (
            self.check_zip,
            self.check_gzip,
            self.check_xz,
        )
        return self.check_multiple_or(payload, checks)

    def check_zip(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.ARCHIVE_PKZIP)

    def check_gzip(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.ARCHIVE_GZIP)

    def check_xz(self, payload: bytes) -> bool:
        return self.check_format(payload, self.FileTypes.ARCHIVE_XZ)

    @staticmethod
    def check_multiple_or(payload: bytes, checks: Tuple[CheckFunction, ...]) -> bool:
        for check in checks:  # type: CheckFunction
            if check(payload):
                return True
        return False

    @staticmethod
    def check_format(payload: bytes, magic_numbers: MagicNumber) -> bool:
        """
        Checks the format against provided magic numbers, returns True if it matches,
        False if it doesn't
        """
        if len(magic_numbers) == 0:
            return False

        check_outcome: bool = False

        for magic_pairs in magic_numbers:  # type: tuple
            pairs_len: int = len(magic_pairs)
            assert (pairs_len % 2) == 0

            for pos in range(0, pairs_len, 2):  # type: int
                offset: int = magic_pairs[pos]
                values: bytes = magic_pairs[pos + 1]
                values_len: int = len(values) + offset
                working_payload: bytes = payload[offset:values_len]

                if working_payload == values and pos == 0:
                    # This is first/only pair in the magic_numbers to check, check_outcome is True
                    check_outcome = True
                elif working_payload == values and pos > 0 and check_outcome is True:
                    # We are deeper in pairs of the magic_numbers, we want previous checks to also be True
                    check_outcome = True
                else:
                    # If both above conditions are broken, check_outcome is False
                    check_outcome = False

            # Above checks didn't exit, format seems to fit
            if check_outcome is True:
                break

        return check_outcome


if __name__ == "__main__":
    main()

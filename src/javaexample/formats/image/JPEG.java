package javaexample.formats.image;

import javaexample.type.MagicNumberSet;
import javaexample.type.SingleMagicNumber;

import javax.xml.bind.DatatypeConverter;
import java.util.ArrayList;

public class JPEG extends javaexample.type.FormatMagicNumbers {

    public JPEG() {
        FormatMagicNumbers = new ArrayList<MagicNumberSet>() {{
            add(new MagicNumberSet(
                    new SingleMagicNumber(0, DatatypeConverter.parseHexBinary("FFD8FFDB"))
            ));
            add(new MagicNumberSet(
                    new SingleMagicNumber(0, DatatypeConverter.parseHexBinary("FFD8FFE000104A4649460001"))
            ));
            add(new MagicNumberSet(
                    new SingleMagicNumber(0, DatatypeConverter.parseHexBinary("FFD8FFEE"))
            ));
            add(new MagicNumberSet(
                    new SingleMagicNumber(0, DatatypeConverter.parseHexBinary("FFD8FFE1")),
                    new SingleMagicNumber(6, DatatypeConverter.parseHexBinary("457869660000"))
            ));
        }};
    }
}

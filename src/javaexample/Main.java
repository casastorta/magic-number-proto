package javaexample;

import javaexample.formats.image.JPEG;

import java.io.FileInputStream;
import java.io.InputStream;

public class Main
{
    static int MaxPayloadSize = 40;

    public static void main(String[] args) throws Exception {
        byte[] inputPayload = new byte[MaxPayloadSize];

        String filename = args[0];
        InputStream inputStream = new FileInputStream(filename);
        inputStream.read(inputPayload);

        JPEG jpegChecker = new JPEG();

        System.out.printf("%s is JPEG?: %s\n", filename, jpegChecker.CheckPayload(inputPayload));
    }
}

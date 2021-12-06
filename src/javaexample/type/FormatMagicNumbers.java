package javaexample.type;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class FormatMagicNumbers {
    protected List<MagicNumberSet> FormatMagicNumbers;

    public boolean CheckPayload(byte[] payload) throws Exception {
        if (payload.length == 0) {
            throw new Exception("Empty payload");
        }

        boolean checkOutcome = false;

        for (MagicNumberSet magicNumberSet : FormatMagicNumbers) {
            Iterator<SingleMagicNumber> singleMagicNumberIterator = magicNumberSet.MagicNumbers.listIterator();
            int counter = 0;
            while (singleMagicNumberIterator.hasNext()) {
                SingleMagicNumber singleMagicNumber = singleMagicNumberIterator.next();

                int offset = singleMagicNumber.Offset;
                byte[] bytes = singleMagicNumber.Bytes;

                int valuesLength = bytes.length + offset;

                if (payload.length < valuesLength) {
                    checkOutcome = false;
                    break;
                }

                byte[] workingPayload = Arrays.copyOfRange(payload, offset, valuesLength);
                boolean comparisonStatus = Arrays.equals(workingPayload, bytes);

                if (comparisonStatus && counter == 0) {
                    checkOutcome = true;
                } else checkOutcome = comparisonStatus && counter > 0 && checkOutcome;

                counter++;
            }

            if (checkOutcome) {
                break;
            }
        }

        return checkOutcome;
    }
}

package javaexample.type;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MagicNumberSet {
    public List<SingleMagicNumber> MagicNumbers = new ArrayList<>();

    public MagicNumberSet(SingleMagicNumber... magicNumbers) {
        MagicNumbers.addAll(Arrays.asList(magicNumbers));
    }
}

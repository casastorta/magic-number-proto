package types

import (
	"bytes"
	"errors"
)

type SingleMagicNumber struct {
	Offset int
	Bytes  []byte
}

type MagicNumberSet struct {
	MagicNumbers []SingleMagicNumber
}

type FormatMagicNumbers struct {
	FormatMagicNumbers []MagicNumberSet
}

func (fmn *FormatMagicNumbers) CheckPayload(payload *[]byte) (bool, error) {
	if len(*payload) == 0 {
		return false, errors.New("Empty payload")
	}

	checkOutcome := false

	for _, magicNumberSet := range fmn.FormatMagicNumbers {
		for pos, singleMagicNumberSet := range magicNumberSet.MagicNumbers {
			offset := singleMagicNumberSet.Offset
			values := singleMagicNumberSet.Bytes
			valuesLen := len(values) + offset

			if len(*payload) < valuesLen {
				checkOutcome = false
				break
			}

			workingPayload := (*payload)[offset:valuesLen]
			comparisonStatus := bytes.Compare(values, workingPayload)

			if comparisonStatus == 0 && pos == 0 {
				checkOutcome = true
			} else if comparisonStatus == 0 && pos > 0 && checkOutcome == true {
				checkOutcome = true
			} else {
				checkOutcome = false
			}
		}

		if checkOutcome == true {
			break
		}

	}
	return checkOutcome, nil
}

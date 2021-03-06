ssi-cdph-2012
=============

Unlocking CA Hospital Surgical Site Infection 2012 data

> What’s in Tables 1 to 24? These tables display each hospital that submitted data on the procedure category with the numbers of procedures and infections, the risk adjusted SIR, and its 95 percent confidence interval with a comparison based on the confidence interval indicating an infection count that was lower, no different or higher than predicted.

More information [here](http://www.cdph.ca.gov/programs/hai/Pages/SurgicalSiteInfections-Report.aspx).

You'll need:
* [qpdf](http://qpdf.sourceforge.net/) for decryption
* [pdftotext](http://www.bluem.net/en/mac/packages/) for text conversion and document layout preservation
* [Pandas](http://pandas.pydata.org/) for data munging

Make sure both `dostuff.sh` and `ssi2012.py` are the ONLY documents in the same directory. Then run `dostuff.sh`. Boom.

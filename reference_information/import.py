import xml.etree.ElementTree as ElT

from reference_information.models import Diagnosis


def save_xml():
    file_dir = "./ICD-10.xml"
    icd_codes = ElT.parse(file_dir)
    diagnoses = icd_codes.findall("record")
    for diagnosis in diagnoses:
        icd_code = diagnosis.find("icd_code").text
        title = diagnosis.find("title").text
        description = diagnosis.find("description").text

        x = Diagnosis.objects.create(
            icd_code=icd_code, title=title, description=description
        )
        x.save()

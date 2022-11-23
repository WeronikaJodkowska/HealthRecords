import xml.etree.ElementTree as ElT

from reference_information.models import Diagnosis, HealthTest, Symptom


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


def save_xml_symptoms():
    file_dir = "../staticfiles/symptoms.xml"
    records = ElT.parse(file_dir)
    symptoms = records.findall("record")
    for symptom in symptoms:
        title = symptom.find("title").text

        x = Symptom.objects.create(title=title)
        x.save()


def save_xml_tests():
    file_dir = "./staticfiles/laboratory-test.xml"
    records = ElT.parse(file_dir)
    tests = records.findall("record")
    for test in tests:
        test_code = test.find("test_code").text
        title = test.find("title").text

        x = HealthTest.objects.create(test_code=test_code, title=title)
        x.save()

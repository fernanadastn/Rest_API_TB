from django.db import models

# Create your models here.
 
import glob
import re

# In[61]:


class XRayImageMetadata:
    def __init__(self, **kwargs):
        self.age = kwargs.get('age', None)
        self.gender = kwargs.get('gender', None)
        self.filename = kwargs.get('filename', None)
        self.report = kwargs.get('report', None)
    def __str__(self):
        return f"<{self.filename}>:{self.gender}-{self.age} years -{self.report}"

            
class XRayMetadataReader:
    def __init__(self, folder, **kwargs):
        self.xrays = []
        self.folder = folder
        self.filenames = glob.glob(kwargs.get('filenames'))
        print(type('filename'))

    def get_filenames(self):
        return self.filenames


class MontgomeryXRayMetadataReader(XRayMetadataReader):
    """
    Normally the first line is something like:
    <Patient's Sex: (the first letter of the gender, like F or M)>
    the second line:
    <Patient's Age: (number with 3 digits Y)>
    the third line:
    <report>
    
    """
# Sexo do paciente aqui!

    def patient_gender(self, firstline):
        gender = None
        if 'F' in firstline:
            gender = 'female'
        elif 'M' in firstline:
            gender = 'male'
        return gender

    def patient_age(self, secondline):
        try:
            age = int(re.findall('d+', secondline)[0])    
        except IndexError:
            age = None
        return age

# Os arquivos serão lidos aqui!
    def read_files(self):
        DataMontgomery = []
        for file in self.get_filenames():
            with open(file) as txtfile:
                content = txtfile.read()
                lines = content.split('\n')
                lines = [l.strip() for l in lines]
                gender = self.patient_gender(lines[0])
                age = self.patient_age(lines[1])
                report = lines[2]
                xray = XRayImageMetadata(gender = gender, age = age, filename = file, report = report)
                DataMontgomery.append(xray)
        return DataMontgomery

path = ('C:/Users/Fê/APITB/MontgomerySets/ClinicalReadings/*.txt')  
Montgomery = MontgomeryXRayMetadataReader("C:/Users/Fê/APITB/MontgomerySets/ClinicalReadings/*.txt")
DataMontgomery = Montgomery.read_files()




import os
import fnmatch
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser
from resumeParser import skillExtractRes

resumes = []
for path,dirs,files in os.walk('resume'):
    for f in fnmatch.filter(files,'*.pdf'):
        resumes.append(os.path.abspath(os.path.join(path,f)))
            
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
resSkill = {}
for i in resumes:
    data = extract_text_from_pdf(i)
    filename = os.path.basename(i)
    domain,skill_list = skillExtractRes(i)
    list(skill_List)
    resSkill[filename] = domain
print(resSkill)
print(skill_list)


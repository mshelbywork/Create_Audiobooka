import re
import pymupdf

def parse_from_toc(toc, doc):
    chapters = []
    for i, entry in enumerate(toc):
        level, title, start_page = entry
        if level == 1:
            end_page = toc[i + 1][2] if i + 1 < len(toc) else len(doc)
            text = ""
            for page_num in range(start_page - 1, end_page - 1):
                text += doc[page_num].get_text()
            chapters.append({"title": title, "text": text.strip()})
    return chapters

def parse_from_regex(doc):
    chapters = []
    current_chapter = None
    current_text = ""
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        match = re.search(r'(Chapter\s+\w+[:\s].+)', text, re.IGNORECASE)
        if match:
            if current_chapter:
                chapters.append({"title": current_chapter, "text": current_text.strip()})
            current_chapter = match.group(1).strip()
            current_text = text[match.end():]
        else:
            current_text += text
    if current_chapter:
        chapters.append({"title": current_chapter, "text": current_text.strip()})
    return chapters

def pdf_parser(filename):
    doc = pymupdf.open(filename)
    toc = doc.get_toc()
    if toc:
        chapters = parse_from_toc(toc, doc)
    else:
        chapters = parse_from_regex(doc)
    return chapters

print (pdf_parser('Effective Communication Skills.pdf'))
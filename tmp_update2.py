import os

files_to_update = [
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\index.html",
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\en\index.html",
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\hybrid\index.html"
]

exact_reps = {
    # Hindi
    'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें।"': 
    'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"',
    
    'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण।"': 
    'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"',
    
    # Korean
    'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다."': 
    'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다."',
    
    'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다."': 
    'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다."',
    
    # Portuguese
    'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente."': 
    'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente. *Basicamente gratuito, com licença Pro disponível para compra."',
    
    'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem."': 
    'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem. *Basicamente gratuito, com licença Pro disponível para compra."',
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for k, v in exact_reps.items():
        content = content.replace(k, v)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")

for f in files_to_update:
    if os.path.exists(f):
        update_file(f)
    else:
        print(f"File not found: {f}")

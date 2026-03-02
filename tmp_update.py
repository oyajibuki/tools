import os
import re

files_to_update = [
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\index.html",
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\en\index.html",
    r"c:\Users\User\Desktop\my-sideprojects\00.tools\hybrid\index.html"
]

html_target = """            <div class="link-row">
              <a href="https://oyajibuki.booth.pm/" target="_blank" class="pro" data-i18n="btn_pro">Pro / 有料版</a>
              <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"
                rel="noopener noreferrer">YouTube</a>
            </div>"""

html_target_alt = """                        <div class="link-row">
                            <a href="https://oyajibuki.booth.pm/" target="_blank" class="pro" data-i18n="btn_pro">Pro /
                                有料版</a>
                            <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"
                                rel="noopener noreferrer">YouTube</a>
                        </div>"""

html_replacement_1 = """            <div class="link-row">
              <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"
                rel="noopener noreferrer">YouTube</a>
            </div>"""

html_replacement_2 = """                        <div class="link-row">
                            <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"
                                rel="noopener noreferrer">YouTube</a>
                        </div>"""

replacements = {
    # hy
    'desc_subtitle_ja: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。',
    'desc_subtitle_en: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files.',
    'desc_clearcut_ja: "画像の切り抜きをするツール",',
    'desc_clearcut_en: "An image background removal and cutout tool.",',
    # en
    'desc_subtitle: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files.",',
    'desc_clearcut: "An image background removal and cutout tool.",',
    # ja
    'desc_subtitle: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。",',
    'desc_clearcut: "画像の切り抜きをするツール",',
    # zh
    'desc_subtitle: "上传视频或音频文件，让人工智能（Whisper）自动转录并生成字幕文件。",',
    'desc_clearcut: "一款基于AI的图像背景去除和抠图工具。",',
    # hi
    'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें。",',
    'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण。",',
    # ko
    'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다。",',
    'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다。",',
    # pt
    'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente。",',
    'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem。",',
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. HTML Replacement
    if html_target in content:
        content = content.replace(html_target, html_replacement_1)
    elif html_target_alt in content:
        content = content.replace(html_target_alt, html_replacement_2)
    else:
        # Fallback regex just in case
        content = re.sub(
            r'<div class="link-row">\s*<a href="https://oyajibuki\.booth\.pm/" target="_blank" class="pro" data-i18n="btn_pro">Pro / 有料版</a>\s*<a href="https://www\.youtube\.com/watch\?v=cBqGlkcqztM" class="youtube" target="_blank"\s*rel="noopener noreferrer">YouTube</a>\s*</div>',
            r'<div class="link-row">\n              <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"\n                rel="noopener noreferrer">YouTube</a>\n            </div>',
            content
        )
        content = re.sub(
            r'<div class="link-row">\s*<a href="https://oyajibuki\.booth\.pm/" target="_blank" class="pro" data-i18n="btn_pro">Pro /\s*有料版</a>\s*<a href="https://www\.youtube\.com/watch\?v=cBqGlkcqztM" class="youtube" target="_blank"\s*rel="noopener noreferrer">YouTube</a>\s*</div>',
            r'<div class="link-row">\n                            <a href="https://www.youtube.com/watch?v=cBqGlkcqztM" class="youtube" target="_blank"\n                                rel="noopener noreferrer">YouTube</a>\n                        </div>',
            content
        )

    # 2. String replacements
    reps = [
        (r'desc_subtitle_ja: "動画や音声をアップロードするだけで、AI\(Whisper\)が自動で文字起こしを行い字幕ファイルを生成します。"',
         r'desc_subtitle_ja: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。※基本無料ですがPro版ライセンスも購入可能です。"'),
        (r'desc_subtitle_en: "Upload a video or audio file and let AI \(Whisper\) automatically transcribe and generate subtitle files."',
         r'desc_subtitle_en: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files. *Basically free, with a Pro license available for purchase."'),
        (r'desc_clearcut_ja: "画像の切り抜きをするツール"',
         r'desc_clearcut_ja: "画像の切り抜きをするツール ※基本無料ですがPro版ライセンスも購入可能です。"'),
        (r'desc_clearcut_en: "An image background removal and cutout tool\."',
         r'desc_clearcut_en: "An image background removal and cutout tool. *Basically free, with a Pro license available for purchase."'),
        
        (r'desc_subtitle: "Upload a video or audio file and let AI \(Whisper\) automatically transcribe and generate subtitle files."',
         r'desc_subtitle: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files. *Basically free, with a Pro license available for purchase."'),
        (r'desc_clearcut: "An image background removal and cutout tool\."',
         r'desc_clearcut: "An image background removal and cutout tool. *Basically free, with a Pro license available for purchase."'),
         
        (r'desc_subtitle: "動画や音声をアップロードするだけで、AI\(Whisper\)が自動で文字起こしを行い字幕ファイルを生成します。"',
         r'desc_subtitle: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。※基本無料ですがPro版ライセンスも購入可能です。"'),
        (r'desc_clearcut: "画像の切り抜きをするツール"',
         r'desc_clearcut: "画像の切り抜きをするツール ※基本無料ですがPro版ライセンスも購入可能です。"'),

        (r'desc_subtitle: "上传视频或音频文件，让人工智能（Whisper）自动转录并生成字幕文件。"',
         r'desc_subtitle: "上传视频或音频文件，让人工智能（Whisper）自动转录并生成字幕文件。*基本免费，可购买专业版许可证。"'),
        (r'desc_clearcut: "一款基于AI的图像背景去除和抠图工具。"',
         r'desc_clearcut: "一款基于AI的图像背景去除和抠图工具。*基本免费，可购买专业版许可证。"'),

        (r'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई \(विस्पर\) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें。"',
         r'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"'),
        (r'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण。"',
         r'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"'),
         
        (r'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई \(विस्पर\) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें。"',
         r'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"'),
        (r'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण。"',
         r'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है।"'),

        (r'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI\(Whisper\)가 자동으로 전사하고 자막 파일을 생성합니다。"',
         r'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다."'),
        (r'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다。"',
         r'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다."'),

        (r'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI \(Whisper\) transcrever e gerar legendas automaticamente。"',
         r'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente. *Basicamente gratuito, com licença Pro disponível para compra."'),
        (r'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem。"',
         r'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem. *Basicamente gratuito, com licença Pro disponível para compra."'),
         
        # Fix for correct quotes (the previous list used 。 for some by mistake in my regex thinking, let's just use exact match on content)
    ]
    
    # Actually, simpler exact string replacements to avoid regex escaping headaches:
    exact_reps = {
        'desc_subtitle_ja: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。': 'desc_subtitle_ja: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。※基本無料ですがPro版ライセンスも購入可能です。',
        'desc_subtitle_en: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files.': 'desc_subtitle_en: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files. *Basically free, with a Pro license available for purchase.',
        'desc_clearcut_ja: "画像の切り抜きをするツール"': 'desc_clearcut_ja: "画像の切り抜きをするツール ※基本無料ですがPro版ライセンスも購入可能です。"',
        'desc_clearcut_en: "An image background removal and cutout tool."': 'desc_clearcut_en: "An image background removal and cutout tool. *Basically free, with a Pro license available for purchase."',
        
        'desc_subtitle: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files."': 'desc_subtitle: "Upload a video or audio file and let AI (Whisper) automatically transcribe and generate subtitle files. *Basically free, with a Pro license available for purchase."',
        'desc_clearcut: "An image background removal and cutout tool."': 'desc_clearcut: "An image background removal and cutout tool. *Basically free, with a Pro license available for purchase."',
        
        'desc_subtitle: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。"': 'desc_subtitle: "動画や音声をアップロードするだけで、AI(Whisper)が自動で文字起こしを行い字幕ファイルを生成します。※基本無料ですがPro版ライセンスも購入可能です。"',
        'desc_clearcut: "画像の切り抜きをするツール"': 'desc_clearcut: "画像の切り抜きをするツール ※基本無料ですがPro版ライセンスも購入可能です。"',
        
        'desc_subtitle: "上传视频或音频文件，让人工智能（Whisper）自动转录并生成字幕文件。"': 'desc_subtitle: "上传视频或音频文件，让人工智能（Whisper）自动转录并生成字幕文件。*基本免费，可购买专业版许可证。"',
        'desc_clearcut: "一款基于AI的图像背景去除和抠图工具。"': 'desc_clearcut: "一款基于AI的图像背景去除和抠图工具。*基本免费，可购买专业版许可证。"',
        
        'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें。"': 'desc_subtitle: "एक वीडियो या ऑडियो फ़ाइल अपलोड करें और एआई (विस्पर) को स्वचालित रूप से ट्रांसक्राइब करने और उपशीर्षक फ़ाइलें बनाने दें। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है。"',
        'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण。"': 'desc_clearcut: "एक छवि पृष्ठभूमि हटाने और कटआउट उपकरण। *मूल रूप से निःशुल्क, प्रो लाइसेंस खरीद के लिए उपलब्ध है。"',
        
        'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다。"': 'desc_subtitle: "비디오 또는 오디오 파일을 업로드하면 AI(Whisper)가 자동으로 전사하고 자막 파일을 생성합니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다。"',
        'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다。"': 'desc_clearcut: "이미지 배경 제거 및 누끼 따기 도구입니다. *기본적으로 무료이며 Pro 라이선스 구매도 가능합니다。"',
        
        'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente。"': 'desc_subtitle: "Faça upload de vídeo ou áudio e deixe a AI (Whisper) transcrever e gerar legendas automaticamente. *Basicamente gratuito, com licença Pro disponível para compra。"',
        'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem。"': 'desc_clearcut: "Uma ferramenta de remoção de fundo e recorte de imagem. *Basicamente gratuito, com licença Pro disponível para compra。"',
    }
    
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

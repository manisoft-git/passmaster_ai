#!/usr/bin/env python3
"""
PassMaster AI — Socratic JAMB & WAEC Exam Coach
In-Depth Technical Presentation Video Generator
720p 16:9, red/gold cybernetic slides, neural voiceover, ambient music.
"""

import os, subprocess
from PIL import Image, ImageDraw, ImageFont

BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR  = os.path.join(BASE_DIR, "static")
TEMP_DIR    = "/tmp/passmaster_video_build"
FINAL_VIDEO = os.path.join(OUTPUT_DIR, "passmaster_ai_presentation.mp4")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

WIDTH, HEIGHT, FPS = 1280, 720, 25

BG_DEEP  = (15, 4, 4)
BG_CARD  = (25, 8, 8)
ACCENT1  = (255, 60, 60)    # red
ACCENT2  = (255, 190, 40)   # gold
ACCENT3  = (60, 200, 255)   # cyan
TEXT_HI  = (255, 240, 240)
TEXT_MID = (220, 180, 180)
GRID_COL = (50, 15, 15)

def lf(path, size):
    try:    return ImageFont.truetype(path, size)
    except: return ImageFont.load_default()

def grid(draw):
    for x in range(0, WIDTH, 60):
        draw.line([(x,0),(x,HEIGHT)], fill=(*GRID_COL,18))
    for y in range(0, HEIGHT, 60):
        draw.line([(0,y),(WIDTH,y)], fill=(*GRID_COL,18))

def glow(draw, x1, y1, x2, y2, col):
    for i in range(5, 0, -1):
        draw.rectangle([x1-i,y1-i,x2+i,y2+i], outline=(*col[:3], int(35*i/5)))
    draw.rectangle([x1,y1,x2,y2], outline=(*col[:3],200), width=2)

def badge(draw, x, y, label, col, font):
    tw = int(draw.textlength(label, font=font))
    p  = 10
    draw.rounded_rectangle([x,y,x+tw+p*2,y+28], radius=6,
                            fill=(*col[:3],35), outline=(*col[:3],180), width=1)
    draw.text((x+p, y+4), label, font=font, fill=col)
    return tw+p*2+8

SCENES = [
    {
        "title": "PASSMASTER AI",
        "subtitle": "Socratic JAMB & WAEC Exam Coach for Nigerian Students",
        "body": [
            "Stop memorising past questions — master the concepts",
            "AI detects WHY you failed, not just that you failed",
            "Socratic step-by-step coaching on every wrong answer",
            "Leaky Bucket Diagnostics — finds exact weak micro-topics",
            "JAMB Score Predictor — Bayesian prediction out of 400",
        ],
        "tags": ["Flask", "Python", "AI Coach", "JAMB", "WAEC"],
        "voiceover": (
            "PassMaster A-I. The next-generation exam mastery engine for Nigerian and African students. "
            "Unlike apps that just show you a static answer, PassMaster detects exactly why you failed a question — "
            "the cognitive trap you fell into — and coaches you step by step, using the Socratic method. "
            "It identifies the exact micro-topics where you are losing JAMB marks. "
            "And a Bayesian Score Predictor tells you your likely score out of four hundred "
            "based on your current performance."
        ),
    },
    {
        "title": "SOCRATIC AI TUTOR",
        "subtitle": "The Engine That Beats Static Answer Apps",
        "body": [
            "Detects cognitive trap type: memory, reasoning, or concept gap",
            "Asks guiding questions instead of just giving answers",
            "Breaks complex topics into digestible micro-steps",
            "Tracks which explanations resonated — adapts over time",
            "Covers all JAMB subjects: English, Maths, Physics, Chemistry",
        ],
        "tags": ["Socratic Method", "Cognitive Analysis", "Adaptive AI", "NLP", "JAMB Syllabus"],
        "voiceover": (
            "The Socratic AI Tutor is the heart of PassMaster. "
            "When you get a question wrong, it doesn't just give you the answer. "
            "It first classifies the type of error — was it a memory failure, a reasoning gap, "
            "or a fundamental concept misunderstanding? "
            "Then it asks you guiding questions to lead you to the answer yourself. "
            "It breaks complex topics into digestible micro-steps. "
            "And it tracks which explanations worked for you — adapting its coaching style over time. "
            "It covers all JAMB subjects: English, Mathematics, Physics, and Chemistry."
        ),
    },
    {
        "title": "LEAKY BUCKET DIAGNOSTICS",
        "subtitle": "Pinpoint Exactly Where You Lose Marks",
        "body": [
            "Maps every question to an official JAMB syllabus micro-topic",
            "Tracks your error rate per micro-topic across all sessions",
            "Generates a personalised 'Leaky Bucket' weakness report",
            "Example: 'You lose marks on Gas Laws in Kelvin (82% error)'",
            "Prioritises weakest topics for targeted drill sessions",
        ],
        "tags": ["Syllabus Mapping", "Error Tracking", "Weak Topic Report", "Targeted Drills", "Analytics"],
        "voiceover": (
            "The Leaky Bucket Diagnostics system maps every question to an official JAMB syllabus micro-topic. "
            "It tracks your error rate per micro-topic across all your sessions. "
            "Then it generates a personalised Leaky Bucket report — showing you exactly where you bleed marks. "
            "For example: You lose marks on Gas Laws in Kelvin with an eighty-two percent error rate. "
            "Those topics become the focus of your next drill session. "
            "This is precision exam preparation — not random past-question grinding."
        ),
    },
    {
        "title": "WHATSAPP LEARNING BOT",
        "subtitle": "Study on Cheap Social Data — No High-Speed Internet Needed",
        "body": [
            "Full JAMB coaching delivered directly on WhatsApp",
            "Works on cheap ₦50/day social data bundles",
            "Students can drill questions, get coaching, check scores",
            "Twilio + WhatsApp Cloud API webhook integration",
            "Zero barrier to entry for rural and low-income students",
        ],
        "tags": ["WhatsApp API", "Twilio", "Cloud API", "Social Data", "Accessibility"],
        "voiceover": (
            "Many Nigerian students cannot afford high-speed internet data. "
            "PassMaster solves this with its WhatsApp Learning Bot. "
            "Full Socratic coaching is delivered directly on WhatsApp — "
            "using cheap fifty naira social data bundles that work even in rural areas. "
            "Students can drill questions, receive step-by-step coaching, and check their predicted score "
            "all from a WhatsApp chat. "
            "The bot is powered by Twilio and the WhatsApp Cloud A-P-I. "
            "Zero barrier to entry. Every student deserves to pass JAMB."
        ),
    },
    {
        "title": "MONETISATION ENGINE",
        "subtitle": "Paystack, Monnify & Scratch-Card Voucher System",
        "body": [
            "Weekly Drill Pass  — ₦1,500 / 7 days unlimited coaching",
            "Monthly Master Pass — ₦3,500 / 30 days + CBT mocks",
            "Full Season Guarantee — ₦8,500 + 280+ score guarantee",
            "Paystack & Monnify virtual accounts for payment",
            "12-digit scratch-card PIN redemption for offline resellers",
        ],
        "tags": ["Paystack", "Monnify", "Voucher Pins", "Subscription", "Monetisation"],
        "voiceover": (
            "PassMaster has a full monetisation engine built in. "
            "The Weekly Drill Pass at one thousand five hundred naira gives seven days of unlimited coaching. "
            "The Monthly Master Pass at three thousand five hundred naira adds full Computer-Based Test mocks. "
            "The Full Season Guarantee at eight thousand five hundred naira guarantees a two-eighty-plus JAMB score. "
            "Payments are processed via Paystack and Monnify virtual accounts. "
            "And a twelve-digit scratch-card voucher system lets tutorial centres and offline resellers "
            "sell access without internet — a critical feature for Nigerian market penetration."
        ),
    },
    {
        "title": "ARCHITECTURE & IMPACT",
        "subtitle": "Built to Scale Across Nigeria & Africa",
        "body": [
            "Flask REST API — lightweight, fast, deployable anywhere",
            "SQLite + JSON question bank — zero-config database",
            "PWA-ready — installable on any Android phone",
            "2 million+ JAMB candidates take the exam every year",
            "Target: top EdTech product in West Africa by 2027",
        ],
        "tags": ["Flask", "PWA", "SQLite", "EdTech", "Nigeria"],
        "voiceover": (
            "PassMaster is built on Python Flask with a zero-config SQLite database and a JSON question bank. "
            "It is Progressive Web App ready — meaning any student can install it on their Android phone "
            "directly from the browser. "
            "Over two million candidates sit the JAMB exam every year in Nigeria. "
            "PassMaster targets every single one of them. "
            "Built by Manifest Subeno, PassMaster A-I is designed to become "
            "the leading EdTech product in West Africa by twenty twenty-seven."
        ),
    },
]

def render_scene(scene, idx):
    img  = Image.new("RGB", (WIDTH, HEIGHT), BG_DEEP)
    draw = ImageDraw.Draw(img, "RGBA")
    grid(draw)

    fn_sm = lf(FONT_MONO, 13)
    draw.text((40, 22), f"SCENE {idx+1:02d}/{len(SCENES):02d}  //  PASSMASTER AI",
              font=fn_sm, fill=(*ACCENT1[:3], 160))
    draw.rectangle([40,44,WIDTH-40,46], fill=ACCENT1)
    draw.rectangle([40,47,WIDTH//2,48], fill=(*ACCENT2[:3],120))

    ft = lf(FONT_BOLD, 46)
    draw.text((40, 62), scene["title"], font=ft, fill=TEXT_HI)
    fs = lf(FONT_REG, 20)
    draw.text((40, 118), scene["subtitle"], font=fs, fill=ACCENT2)

    cy, ch = 155, 340
    draw.rounded_rectangle([30,cy,WIDTH-30,cy+ch], radius=12, fill=(*BG_CARD,220))
    glow(draw, 30, cy, WIDTH-30, cy+ch, ACCENT1)

    fb = lf(FONT_REG, 19)
    for i, line in enumerate(scene["body"]):
        y = cy + 22 + i*52
        draw.ellipse([50,y+7,60,y+17], fill=ACCENT2)
        draw.text((72, y), line, font=fb, fill=TEXT_MID)
        draw.line([(72,y+32),(WIDTH-50,y+32)], fill=(*GRID_COL,60))

    tag_y = cy+ch+22
    fm = lf(FONT_MONO, 14)
    xc = 40
    for tag in scene["tags"]:
        xc += badge(draw, xc, tag_y, tag, ACCENT3, fm)

    draw.rectangle([40, HEIGHT-44, WIDTH-40, HEIGHT-42], fill=(*ACCENT1[:3],60))
    draw.text((40, HEIGHT-36), "PASSMASTER AI  //  SOCRATIC JAMB & WAEC EXAM COACH",
              font=fn_sm, fill=(*ACCENT1[:3],100))

    fd = os.path.join(TEMP_DIR, f"s{idx:02d}"); os.makedirs(fd, exist_ok=True)
    p  = os.path.join(fd, "frame.png"); img.save(p); return p

def synth(text, out):
    try:
        r = subprocess.run(["edge-tts","--voice","en-US-ChristopherNeural","--rate","+5%",
                            "--text",text,"--write-media",out],capture_output=True,timeout=120)
        if r.returncode==0 and os.path.exists(out): return True
    except: pass
    try: subprocess.run(["gtts-cli","--lang","en",text,"--output",out],capture_output=True,timeout=90)
    except: pass
    return os.path.exists(out)

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","default=noprint_wrappers=1:nokey=1",path],capture_output=True,text=True)
    try: return float(r.stdout.strip())
    except: return 8.0

def make_clip(idx, frame, audio):
    out = os.path.join(TEMP_DIR, f"clip_{idx:02d}.mp4")
    d   = dur(audio)+1.2
    subprocess.run([
        "ffmpeg","-y","-loop","1","-i",frame,"-i",audio,
        "-vf",f"scale={WIDTH}:{HEIGHT},zoompan=z='min(zoom+0.0008,1.04)':d={int(d*FPS)}:s={WIDTH}x{HEIGHT}:fps={FPS}",
        "-c:v","libx264","-preset","fast","-crf","22",
        "-c:a","aac","-b:a","128k","-t",str(d),"-pix_fmt","yuv420p",out
    ], capture_output=True)
    return out

def ambient(duration, out):
    subprocess.run([
        "ffmpeg","-y","-f","lavfi","-i",
        f"aevalsrc=0.06*sin(2*PI*50*t)*exp(-0.3*(t mod 2))+0.04*sin(2*PI*100*t)+0.02*sin(2*PI*200*t):s=44100:d={duration}",
        "-af","aecho=0.5:0.5:70:0.4,lowpass=f=750,volume=0.35",out
    ], capture_output=True)

def main():
    print("="*60)
    print(" PASSMASTER AI — VIDEO PRESENTATION GENERATOR")
    print("="*60)
    clips = []
    for i, scene in enumerate(SCENES):
        print(f"\n📹 Scene {i+1}/{len(SCENES)}: {scene['title']}")
        frame = render_scene(scene, i)
        ao    = os.path.join(TEMP_DIR, f"vo_{i:02d}.mp3")
        synth(scene["voiceover"], ao)
        clips.append(make_clip(i, frame, ao))
        print("  ✅ Done")

    lf_path = os.path.join(TEMP_DIR, "concat.txt")
    with open(lf_path,"w") as f:
        for c in clips: f.write(f"file '{c}'\n")
    raw = os.path.join(TEMP_DIR, "raw.mp4")
    subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",lf_path,"-c","copy",raw],capture_output=True)

    total = dur(raw)
    amb   = os.path.join(TEMP_DIR, "ambient.wav")
    ambient(int(total)+5, amb)

    print("\n🎚  Mastering...")
    subprocess.run([
        "ffmpeg","-y","-i",raw,"-i",amb,
        "-filter_complex","[0:a]volume=1.0[va];[1:a]volume=0.12[vb];[va][vb]amix=inputs=2:duration=first[aout]",
        "-map","0:v","-map","[aout]","-c:v","copy","-c:a","aac","-b:a","144k",FINAL_VIDEO
    ], capture_output=True)

    size = os.path.getsize(FINAL_VIDEO)/(1024*1024)
    d2   = dur(FINAL_VIDEO)
    print(f"\n🎉 {FINAL_VIDEO}")
    print("="*60)
    print(f" [SUCCESS] {WIDTH}x{HEIGHT}  {d2:.1f}s  {size:.2f}MB")
    print("="*60)

if __name__ == "__main__":
    main()

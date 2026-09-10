#!/usr/bin/env python3
"""
PassMaster AI — Walkthrough & Advertisement Video Generator
Produces a high-definition 720p 16:9 video with neural voiceover, modern dark UI slides,
subtitles, Ken Burns pan/zoom animation, and ambient audio bed.
"""

import os
import sys
import glob
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "static")
TEMP_DIR = "/tmp/passmaster_video"
FINAL_VIDEO = os.path.join(OUTPUT_DIR, "passmaster_ai_walkthrough_ad.mp4")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Dimensions
WIDTH = 1280
HEIGHT = 720

# Color Palette (PassMaster AI Theme)
BG_TOP = (11, 17, 32)        # #0b1120 Deep Space Navy
BG_BOTTOM = (7, 11, 20)      # #070b14 Dark Slate
CARD_BG = (22, 33, 56)       # #162138 Card background
CARD_BORDER = (45, 66, 105)  # Border
CYAN = (56, 189, 248)        # #38bdf8 Electric Sky Blue
GREEN = (16, 185, 129)       # #10b981 Emerald
AMBER = (245, 158, 11)       # #f59e0b Amber
RED = (239, 68, 68)          # #ef4444 Danger Red
WHITE = (255, 255, 255)
TEXT_MUTED = (148, 163, 184) # #94a3b8 Slate Muted
PURPLE = (129, 140, 248)     # #818cf8 Soft Indigo

SCENES = [
    {
        "id": "scene1_hook",
        "title": "STUCK BELOW 200 IN JAMB?",
        "subtitle": "Are you still cramming JAMB past questions and stuck below 200? Over 70% of candidates miss top tier university cut-offs because memorization does not work. It is time for a smarter way.",
        "voice_text": "Are you still cramming JAMB past questions and stuck below 200? Over seventy percent of candidates miss top tier university cut-offs because memorization does not work. It is time for a smarter way.",
        "type": "problem"
    },
    {
        "id": "scene2_intro",
        "title": "MEET PASSMASTER AI 🎯",
        "subtitle": "Meet PassMaster AI. The next-generation Socratic exam coach built specifically for Nigerian and African students. Do not just memorize past questions. Master the core concepts and hit 280 plus.",
        "voice_text": "Meet PassMaster AI. The next-generation Socratic exam coach built specifically for Nigerian and African students. Do not just memorize past questions. Master the core concepts and hit 280 plus.",
        "type": "solution"
    },
    {
        "id": "scene3_socratic",
        "title": "FEATURE 1: SOCRATIC ERROR ANALYSIS",
        "subtitle": "Unlike traditional CBT apps that only give a one-line static answer, PassMaster AI detects why you failed. It pinpoints cognitive traps, explains distractor options, and coaches you step-by-step.",
        "voice_text": "Unlike traditional CBT apps that only give a one-line static answer, PassMaster AI detects why you failed. It pinpoints cognitive traps, explains distractor options, and coaches you step-by-step.",
        "type": "socratic"
    },
    {
        "id": "scene4_leaky",
        "title": "FEATURE 2: LEAKY BUCKET DIAGNOSTICS",
        "subtitle": "Stop guessing your weaknesses. Our Leaky Bucket diagnostics engine highlights the exact micro-topics where you are bleeding marks, while our AI predictor tracks your projected score out of four hundred.",
        "voice_text": "Stop guessing your weaknesses. Our Leaky Bucket diagnostics engine highlights the exact micro-topics where you are bleeding marks, while our AI predictor tracks your projected score out of four hundred.",
        "type": "leaky"
    },
    {
        "id": "scene5_whatsapp",
        "title": "FEATURE 3: WHATSAPP AI STUDY BOT",
        "subtitle": "No high-speed internet? No problem! Practice CBT questions, take timed micro-drills, and chat with your 24/7 AI tutor directly on WhatsApp using affordable daily social data.",
        "voice_text": "No high-speed internet? No problem! Practice CBT questions, take timed micro-drills, and chat with your 24/7 AI tutor directly on WhatsApp using affordable daily social data.",
        "type": "whatsapp"
    },
    {
        "id": "scene6_cbt",
        "title": "FEATURE 4: CBT MOCKS & MISTAKE VAULT",
        "subtitle": "Experience authentic JAMB CBT exams with live timers, national leaderboard rankings, and an automatic Mistake Vault that stores your missed questions for smart spaced repetition.",
        "voice_text": "Experience authentic JAMB CBT exams with live timers, national leaderboard rankings, and an automatic Mistake Vault that stores your missed questions for smart spaced repetition.",
        "type": "cbt"
    },
    {
        "id": "scene7_pricing",
        "title": "CRUSH JAMB 2026/2027 • HIT 280+",
        "subtitle": "Unlock your weekly pass for just fifteen hundred Naira, or get the full season guarantee with parent reports and voucher PIN support. Join thousands of students hitting 280 plus. Visit PassMaster AI today!",
        "voice_text": "Unlock your weekly pass for just fifteen hundred Naira, or get the full season guarantee with parent reports and voucher PIN support. Join thousands of students hitting 280 plus. Visit PassMaster AI today!",
        "type": "pricing"
    }
]

def draw_gradient_background(img):
    """Draws a vertical gradient background with ambient decorative circles."""
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        ratio = y / float(HEIGHT)
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # Ambient glows
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([WIDTH - 300, -100, WIDTH + 200, 400], fill=(56, 189, 248, 20))
    ov_draw.ellipse([-100, HEIGHT - 300, 400, HEIGHT + 200], fill=(99, 102, 241, 20))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"))

def draw_header(draw, title_text, badge_text=None):
    """Draws top brand bar with logo and badge."""
    font_logo = ImageFont.truetype(FONT_BOLD, 22)
    font_sub = ImageFont.truetype(FONT_REGULAR, 14)
    font_badge = ImageFont.truetype(FONT_BOLD, 12)
    
    # Brand
    draw.text((60, 40), "🎯 PassMaster AI", fill=CYAN, font=font_logo)
    draw.text((60, 68), "Socratic JAMB & WAEC Exam Coach", fill=TEXT_MUTED, font=font_sub)
    
    # Live target badge
    badge_label = badge_text or "⚡ TARGET: 280+ FOR UNILAG / UI / OAU"
    bbox = font_badge.getbbox(badge_label)
    bw = bbox[2] - bbox[0] + 24
    draw.rounded_rectangle([WIDTH - 60 - bw, 42, WIDTH - 60, 74], radius=16, fill=(16, 185, 129, 40), outline=GREEN, width=1)
    draw.text((WIDTH - 60 - bw + 12, 50), badge_label, fill=GREEN, font=font_badge)

def draw_subtitle_bar(draw, text):
    """Draws sleek closed-caption subtitles at the bottom."""
    font_sub = ImageFont.truetype(FONT_REGULAR, 15)
    
    # Wrap text
    words = text.split()
    lines = []
    curr = ""
    for w in words:
        if len(curr + " " + w) < 95:
            curr = (curr + " " + w).strip()
        else:
            lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)
    
    bar_height = len(lines) * 22 + 20
    bar_y1 = HEIGHT - bar_height - 25
    bar_y2 = HEIGHT - 25
    
    draw.rounded_rectangle([60, bar_y1, WIDTH - 60, bar_y2], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    
    for i, line in enumerate(lines):
        line_y = bar_y1 + 10 + (i * 22)
        draw.text((80, line_y), line, fill=(241, 245, 249), font=font_sub)

def create_scene1_image():
    """Scene 1: Problem / Cramming doesn't work"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "⚠️ 75% OF CANDIDATES FAIL")
    
    font_title = ImageFont.truetype(FONT_BOLD, 36)
    font_h2 = ImageFont.truetype(FONT_BOLD, 20)
    font_body = ImageFont.truetype(FONT_REGULAR, 16)
    font_bigstat = ImageFont.truetype(FONT_BOLD, 48)
    
    draw.text((60, 115), "STUCK BELOW 200 IN JAMB?", fill=RED, font=font_title)
    draw.text((60, 165), "Why memorizing past questions is failing over 1.4 million students every year.", fill=TEXT_MUTED, font=font_body)
    
    # Card 1: The Cramming Trap (Left)
    c1 = [60, 215, 620, 520]
    draw.rounded_rectangle(c1, radius=16, fill=CARD_BG, outline=(239, 68, 68, 120), width=2)
    draw.text((90, 240), "❌ The Rote Memorization Trap", fill=RED, font=font_h2)
    bullets1 = [
        "• Static answer keys give zero understanding of concepts",
        "• Slight twist in syllabus question causes immediate panic",
        "• Students waste 4+ hours daily practicing blindly",
        "• Missing micro-topics (e.g. Gas Laws, Concord) costs 40+ marks"
    ]
    for i, b in enumerate(bullets1):
        draw.text((90, 290 + i * 42), b, fill=(226, 232, 240), font=font_body)
        
    # Card 2: The Harsh Reality (Right)
    c2 = [660, 215, WIDTH - 60, 520]
    draw.rounded_rectangle(c2, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
    draw.text((690, 240), "📊 The Real JAMB Statistics", fill=CYAN, font=font_h2)
    
    draw.text((690, 290), "76.4%", fill=AMBER, font=font_bigstat)
    draw.text((880, 305), "scored below 200 in 2024", fill=TEXT_MUTED, font=font_body)
    
    draw.text((690, 365), "280+", fill=GREEN, font=font_bigstat)
    draw.text((860, 380), "required for Medicine / Law", fill=TEXT_MUTED, font=font_body)
    
    draw.rounded_rectangle([690, 445, WIDTH - 90, 495], radius=10, fill=(30, 41, 59))
    draw.text((710, 460), "💡 Solution: Socratic AI Conceptual Mastery", fill=WHITE, font=font_h2)
    
    draw_subtitle_bar(draw, SCENES[0]["subtitle"])
    return img

def create_scene2_image():
    """Scene 2: Introducing PassMaster AI"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "🚀 NEXT-GEN EXAM ENGINE")
    
    font_title = ImageFont.truetype(FONT_BOLD, 36)
    font_h2 = ImageFont.truetype(FONT_BOLD, 18)
    font_body = ImageFont.truetype(FONT_REGULAR, 15)
    
    draw.text((60, 115), "MEET PASSMASTER AI 🎯", fill=CYAN, font=font_title)
    draw.text((60, 165), "Stop memorizing answers. Master the underlying logic with your 24/7 Socratic AI Coach.", fill=TEXT_MUTED, font=font_body)
    
    # 3 Feature Pillars
    cards = [
        ("🧠 Socratic Error Analysis", "Detects WHY you failed", "Breaks down cognitive traps, explains distractor options, and guides you to the right answer.", CYAN),
        ("📉 Leaky Bucket Engine", "Pinpoints Lost Marks", "Identifies exact micro-topics bleeding your score and dynamically predicts your result out of 400.", GREEN),
        ("💬 WhatsApp Learning Bot", "Zero High-Speed Barrier", "Practice drills, ask questions, and get instant explanations on WhatsApp using cheap daily data.", AMBER)
    ]
    
    card_w = (WIDTH - 120 - 40) // 3
    for i, (title, tag, desc, accent) in enumerate(cards):
        x1 = 60 + i * (card_w + 20)
        x2 = x1 + card_w
        draw.rounded_rectangle([x1, 215, x2, 520], radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
        draw.rounded_rectangle([x1 + 25, 235, x1 + 25 + 10, 275], radius=4, fill=accent)
        draw.text((x1 + 45, 235), title, fill=WHITE, font=font_h2)
        draw.text((x1 + 45, 260), tag, fill=accent, font=font_body)
        
        words = desc.split()
        curr, dlines = "", []
        for w in words:
            if len(curr + " " + w) < 26:
                curr = (curr + " " + w).strip()
            else:
                dlines.append(curr)
                curr = w
        if curr:
            dlines.append(curr)
            
        for dl_idx, dl in enumerate(dlines):
            draw.text((x1 + 25, 310 + dl_idx * 28), dl, fill=(203, 213, 225), font=font_body)
            
        draw.rounded_rectangle([x1 + 25, 455, x2 - 25, 495], radius=8, fill=(30, 41, 59))
        draw.text((x1 + 38, 467), "✓ Active in 2026/2027 Season", fill=GREEN, font=font_body)

    draw_subtitle_bar(draw, SCENES[1]["subtitle"])
    return img

def create_scene3_image():
    """Scene 3: Walkthrough - Socratic Error Analysis"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "FEATURE: SOCRATIC COACHING")
    
    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_h2 = ImageFont.truetype(FONT_BOLD, 18)
    font_body = ImageFont.truetype(FONT_REGULAR, 15)
    
    draw.text((60, 115), "1. Socratic Error Analysis & Cognitive Traps", fill=PURPLE, font=font_title)
    
    # Left: The Question Card
    c1 = [60, 175, 600, 525]
    draw.rounded_rectangle(c1, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
    draw.text((85, 195), "JAMB Use of English — Question #14", fill=CYAN, font=font_h2)
    draw.text((85, 235), "Neither the principal nor the teachers _____ present", fill=WHITE, font=font_body)
    draw.text((85, 260), "at the emergency school meeting yesterday.", fill=WHITE, font=font_body)
    
    options = [
        ("A", "was", False, RED),
        ("B", "were", True, GREEN),
        ("C", "is", False, TEXT_MUTED),
        ("D", "are", False, TEXT_MUTED)
    ]
    for i, (opt, txt, is_corr, col) in enumerate(options):
        oy = 310 + i * 48
        bg_col = (45, 20, 20) if opt == "A" else ((20, 45, 30) if opt == "B" else (26, 36, 56))
        draw.rounded_rectangle([85, oy, 575, oy + 38], radius=8, fill=bg_col, outline=col, width=1)
        badge = "❌ Your Pick" if opt == "A" else ("✅ Correct Answer" if opt == "B" else "")
        draw.text((100, oy + 8), f"({opt})  {txt}", fill=WHITE, font=font_body)
        if badge:
            draw.text((430, oy + 8), badge, fill=col, font=font_body)
            
    # Right: The Socratic AI Coach Card
    c2 = [630, 175, WIDTH - 60, 525]
    draw.rounded_rectangle(c2, radius=16, fill=CARD_BG, outline=PURPLE, width=2)
    draw.text((655, 195), "🤖 PassMaster Socratic Analysis", fill=PURPLE, font=font_h2)
    
    draw.rounded_rectangle([655, 235, WIDTH - 85, 280], radius=8, fill=(88, 28, 135, 60), outline=PURPLE, width=1)
    draw.text((670, 248), "⚠️ Cognitive Trap: Rule of Proximity in Concord", fill=WHITE, font=font_h2)
    
    analysis_lines = [
        "• Why 'was' was picked: You focused on 'principal' (singular).",
        "• The Golden Rule: In 'neither... nor' and 'either... or', the",
        "  verb must agree with the NEAREST subject.",
        "• The nearest subject is 'teachers' (plural noun).",
        "• Therefore: 'teachers WERE present' is correct!",
        "💡 Spaced Repetition: Saved to your Mistake Vault for review."
    ]
    for i, l in enumerate(analysis_lines):
        col = GREEN if "Golden Rule" in l or "Therefore" in l else ((251, 191, 36) if "💡" in l else (226, 232, 240))
        draw.text((655, 300 + i * 34), l, fill=col, font=font_body)
        
    draw_subtitle_bar(draw, SCENES[2]["subtitle"])
    return img

def create_scene4_image():
    """Scene 4: Walkthrough - Leaky Bucket & Score Predictor"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "FEATURE: DIAGNOSTICS")
    
    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_h2 = ImageFont.truetype(FONT_BOLD, 18)
    font_body = ImageFont.truetype(FONT_REGULAR, 15)
    font_big = ImageFont.truetype(FONT_BOLD, 42)
    
    draw.text((60, 115), "2. Leaky Bucket Diagnostics & Score Predictor", fill=GREEN, font=font_title)
    
    # Left: Leaky Topics
    c1 = [60, 175, 620, 525]
    draw.rounded_rectangle(c1, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
    draw.text((85, 195), "📉 Where You Are Bleeding Marks", fill=RED, font=font_h2)
    
    leaks = [
        ("🔴 Physics: Gas Laws & Absolute Temp", "-14 JAMB Marks", "Failed 4 of 5 thermodynamic items"),
        ("🔴 Chemistry: Redox Equations & Oxidation", "-10 JAMB Marks", "Confusing reducing vs oxidizing agents"),
        ("🟡 English: Concord & Proximity Rules", "-8 JAMB Marks", "Trap: Compound subjects joined by 'with'"),
        ("🟢 Biology: Genetics & Punnett Crosses", "Mastered (+18)", "92% accuracy across 20 items")
    ]
    for i, (topic, impact, sub) in enumerate(leaks):
        ly = 240 + i * 66
        draw.rounded_rectangle([85, ly, 595, ly + 56], radius=8, fill=(30, 41, 59))
        draw.text((95, ly + 8), topic, fill=WHITE, font=font_h2)
        col = RED if "-14" in impact else (AMBER if "-10" in impact or "-8" in impact else GREEN)
        draw.text((450, ly + 8), impact, fill=col, font=font_h2)
        draw.text((95, ly + 32), sub, fill=TEXT_MUTED, font=font_body)
        
    # Right: Predicted Score
    c2 = [650, 175, WIDTH - 60, 525]
    draw.rounded_rectangle(c2, radius=16, fill=CARD_BG, outline=GREEN, width=2)
    draw.text((675, 195), "🎯 Bayesian Score Predictor", fill=CYAN, font=font_h2)
    
    draw.text((675, 235), "PROJECTED JAMB SCORE", fill=TEXT_MUTED, font=font_body)
    draw.text((675, 260), "294 / 400", fill=GREEN, font=font_big)
    draw.text((920, 275), "(Top 3.8% Nationally)", fill=AMBER, font=font_h2)
    
    # Progress Bar
    draw.rounded_rectangle([675, 325, WIDTH - 85, 345], radius=10, fill=(30, 41, 59))
    draw.rounded_rectangle([675, 325, 675 + int((WIDTH - 760) * 0.735), 345], radius=10, fill=GREEN)
    
    draw.text((675, 370), "🏛️ University Admission Viability:", fill=WHITE, font=font_h2)
    admissions = [
        ("• UNILAG — Medicine & Surgery:", "High Probability (Cutoff: 285)"),
        ("• University of Ibadan — Pharmacy:", "High Probability (Cutoff: 275)"),
        ("• OAU — Computer Engineering:", "Competitive (Cutoff: 280)")
    ]
    for i, (uni, stat) in enumerate(admissions):
        draw.text((675, 405 + i * 32), uni, fill=CYAN, font=font_body)
        draw.text((965, 405 + i * 32), stat, fill=WHITE, font=font_body)
        
    draw_subtitle_bar(draw, SCENES[3]["subtitle"])
    return img

def create_scene5_image():
    """Scene 5: Walkthrough - WhatsApp Learning Bot"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "FEATURE: WHATSAPP BOT")
    
    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_h2 = ImageFont.truetype(FONT_BOLD, 17)
    font_body = ImageFont.truetype(FONT_REGULAR, 14)
    
    draw.text((60, 115), "3. 24/7 AI Tutor on WhatsApp (Zero High-Speed Data)", fill=AMBER, font=font_title)
    
    # Left: WhatsApp Chat Screen Mockup
    c1 = [60, 165, 640, 530]
    draw.rounded_rectangle(c1, radius=16, fill=(17, 24, 39), outline=(37, 211, 102), width=2)
    
    draw.rounded_rectangle([60, 165, 640, 215], radius=16, fill=(7, 94, 84))
    draw.text((80, 180), "🟢 PassMaster AI Socratic Coach • Online", fill=WHITE, font=font_h2)
    
    # Student bubble
    draw.rounded_rectangle([220, 230, 620, 280], radius=10, fill=(5, 97, 98))
    draw.text((235, 242), "Coach, why is work done ZERO in circular", fill=WHITE, font=font_body)
    draw.text((235, 260), "motion? The object is moving! 🤔", fill=WHITE, font=font_body)
    
    # AI Tutor bubble
    draw.rounded_rectangle([80, 295, 540, 395], radius=10, fill=(31, 41, 55))
    draw.text((95, 305), "🤖 PassMaster Coach:", fill=GREEN, font=font_h2)
    draw.text((95, 328), "Look at the angle θ between force and motion!", fill=(241, 245, 249), font=font_body)
    draw.text((95, 348), "Centripetal force is perpendicular (90°) to path.", fill=(241, 245, 249), font=font_body)
    draw.text((95, 368), "Since cos(90°) = 0, Work = F × d × 0 = 0 Joules!", fill=CYAN, font=font_h2)
    
    # Student follow up
    draw.rounded_rectangle([260, 410, 620, 455], radius=10, fill=(5, 97, 98))
    draw.text((275, 423), "Aha! Perpendicular force does no work! 🙌", fill=WHITE, font=font_body)
    
    draw.rounded_rectangle([80, 475, 620, 515], radius=20, fill=(30, 41, 59))
    draw.text((105, 488), "Type a past question or topic to drill...", fill=TEXT_MUTED, font=font_body)
    
    # Right: Advantages
    c2 = [670, 165, WIDTH - 60, 530]
    draw.rounded_rectangle(c2, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
    draw.text((700, 190), "📱 Zero Data Barrier Learning", fill=GREEN, font=font_h2)
    
    bullets = [
        ("📶 Cheap Daily Social Bundles", "Works with WhatsApp-only data bundles (₦50 - ₦100/day). No laptop needed."),
        ("⚡ 1-Minute Micro-Drills", "Practice 5 questions during commutes, lunch breaks, or before bed."),
        ("🎙️ Voice & Audio Notes", "Listen to AI voice explanations directly in your WhatsApp chats."),
        ("👨‍👩‍👧 Parent Weekly Summary", "Parents receive automated WhatsApp progress reports every Sunday.")
    ]
    for i, (btitle, bdesc) in enumerate(bullets):
        by = 235 + i * 68
        draw.text((700, by), btitle, fill=WHITE, font=font_h2)
        draw.text((700, by + 24), bdesc, fill=TEXT_MUTED, font=font_body)
        
    draw_subtitle_bar(draw, SCENES[4]["subtitle"])
    return img

def create_scene6_image():
    """Scene 6: Walkthrough - Real CBT Mock & Mistake Vault"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "FEATURE: CBT MOCK & VAULT")
    
    font_title = ImageFont.truetype(FONT_BOLD, 32)
    font_h2 = ImageFont.truetype(FONT_BOLD, 17)
    font_body = ImageFont.truetype(FONT_REGULAR, 14)
    
    draw.text((60, 115), "4. Real CBT Exam Simulation & Mistake Vault", fill=CYAN, font=font_title)
    
    # Left: CBT Exam Card
    c1 = [60, 165, 630, 525]
    draw.rounded_rectangle(c1, radius=16, fill=CARD_BG, outline=CARD_BORDER, width=1)
    draw.text((85, 190), "⚡ Official JAMB 180-Question CBT Engine", fill=CYAN, font=font_h2)
    
    features = [
        ("⏱️ Authentic 2-Hour Countdown", "Realistic JAMB interface with 8-key navigation (A, B, C, D, N, P, S, R)."),
        ("📓 Automatic Mistake Vault", "Never repeat an error. All wrong answers are tagged with cognitive traps."),
        ("🔁 Spaced Repetition Drills", "The algorithm resurfaces weak questions 48 hours later to cement recall."),
        ("📊 Instant Subject Mastery", "English (84%), Mathematics (78%), Physics (72%), Chemistry (80%).")
    ]
    for i, (ft, fd) in enumerate(features):
        fy = 230 + i * 68
        draw.text((85, fy), ft, fill=WHITE, font=font_h2)
        draw.text((85, fy + 24), fd, fill=TEXT_MUTED, font=font_body)
        
    # Right: National Leaderboard
    c2 = [660, 165, WIDTH - 60, 525]
    draw.rounded_rectangle(c2, radius=16, fill=CARD_BG, outline=AMBER, width=2)
    draw.text((685, 190), "🏆 National Weekly Leaderboard", fill=AMBER, font=font_h2)
    
    ranks = [
        ("🥇 #1", "Chinedu O. (Anambra)", "348 / 400", "Top 0.1%"),
        ("🥈 #2", "Aisha M. (Kaduna)", "336 / 400", "Top 0.5%"),
        ("🥉 #3", "Femi A. (Lagos)", "324 / 400", "Top 1.2%"),
        ("🎖️ #4", "Blessing E. (Edo)", "312 / 400", "Top 2.0%"),
        ("👤 You", "Target: UNILAG Medicine", "294 / 400", "Top 3.8%")
    ]
    for i, (rank, name, score, pct) in enumerate(ranks):
        ry = 235 + i * 54
        bg_col = (45, 35, 15) if "🥇" in rank else ((30, 41, 59) if "You" in rank else (20, 28, 45))
        draw.rounded_rectangle([685, ry, WIDTH - 85, ry + 46], radius=8, fill=bg_col)
        draw.text((700, ry + 12), rank, fill=AMBER if "#1" in rank else WHITE, font=font_h2)
        draw.text((770, ry + 12), name, fill=WHITE, font=font_body)
        draw.text((1020, ry + 12), score, fill=GREEN if "You" not in rank else CYAN, font=font_h2)
        draw.text((1120, ry + 12), pct, fill=TEXT_MUTED, font=font_body)
        
    draw_subtitle_bar(draw, SCENES[5]["subtitle"])
    return img

def create_scene7_image():
    """Scene 7: Pricing & Call to Action"""
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw_gradient_background(img)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PassMaster AI", "⚡ AFFORDABLE PLANS")
    
    font_title = ImageFont.truetype(FONT_BOLD, 36)
    font_h2 = ImageFont.truetype(FONT_BOLD, 18)
    font_price = ImageFont.truetype(FONT_BOLD, 28)
    font_body = ImageFont.truetype(FONT_REGULAR, 14)
    
    draw.text((60, 110), "START DRILLING TODAY • HIT 280+", fill=GREEN, font=font_title)
    draw.text((60, 155), "Flexible pricing designed for every Nigerian student and tutorial center.", fill=TEXT_MUTED, font=font_body)
    
    # 3 Pricing Cards
    tiers = [
        ("Weekly Drill Pass", "₦1,500", "7 Days Access", [
            "• Unlimited Socratic AI coaching",
            "• 32 Deep Masterclasses",
            "• Daily micro-drills",
            "• Leaky bucket diagnostics"
        ], CYAN, False),
        ("Monthly Master Pass", "₦3,500", "30 Days Access", [
            "• Full CBT Mock Exams (Timed)",
            "• Complete WhatsApp Bot access",
            "• Automatic Mistake Vault",
            "• Spaced Repetition engine"
        ], GREEN, True),
        ("Full Season Guarantee", "₦8,500", "Valid Until Exam Day", [
            "• 280+ JAMB Score Guarantee",
            "• Parent Weekly Progress Portal",
            "• 12-Digit Voucher PIN support",
            "• Priority WhatsApp VIP Coach"
        ], AMBER, False)
    ]
    
    card_w = (WIDTH - 120 - 40) // 3
    for i, (name, price, period, perks, accent, is_popular) in enumerate(tiers):
        x1 = 60 + i * (card_w + 20)
        x2 = x1 + card_w
        border_col = accent if is_popular else CARD_BORDER
        draw.rounded_rectangle([x1, 195, x2, 475], radius=16, fill=CARD_BG, outline=border_col, width=2 if is_popular else 1)
        
        if is_popular:
            draw.rounded_rectangle([x1 + 40, 180, x2 - 40, 205], radius=8, fill=GREEN)
            draw.text((x1 + 65, 185), "🔥 MOST POPULAR", fill=(10, 20, 15), font=font_body)
            
        draw.text((x1 + 25, 220), name, fill=WHITE, font=font_h2)
        draw.text((x1 + 25, 245), price, fill=accent, font=font_price)
        draw.text((x1 + 140, 255), f"/ {period}", fill=TEXT_MUTED, font=font_body)
        
        for p_idx, p in enumerate(perks):
            draw.text((x1 + 25, 305 + p_idx * 32), p, fill=(226, 232, 240), font=font_body)
            
        btn_bg = accent if is_popular else (30, 41, 59)
        draw.rounded_rectangle([x1 + 25, 420, x2 - 25, 458], radius=8, fill=btn_bg)
        btn_text = "Activate Now ⚡" if is_popular else "Get Started"
        draw.text((x1 + 80, 430), btn_text, fill=(10, 20, 15) if is_popular else WHITE, font=font_h2)
        
    draw.text((60, 495), "💳 Pay with Card, Bank Transfer, USSD, or Offline 12-Digit Voucher PINs.", fill=TEXT_MUTED, font=font_body)
    
    draw_subtitle_bar(draw, SCENES[6]["subtitle"])
    return img

def render_all_scene_images():
    """Generates all 7 high-res slide images."""
    generators = [
        ("scene1_hook", create_scene1_image),
        ("scene2_intro", create_scene2_image),
        ("scene3_socratic", create_scene3_image),
        ("scene4_leaky", create_scene4_image),
        ("scene5_whatsapp", create_scene5_image),
        ("scene6_cbt", create_scene6_image),
        ("scene7_pricing", create_scene7_image)
    ]
    for sid, gen in generators:
        img_path = os.path.join(TEMP_DIR, f"{sid}.png")
        img = gen()
        img.save(img_path, quality=95)
        print(f"✓ Rendered slide: {img_path}")

def generate_scene_video(scene, index):
    """Generates an individual animated video clip for a scene using ffmpeg."""
    sid = scene["id"]
    img_path = os.path.join(TEMP_DIR, f"{sid}.png")
    audio_path = f"/tmp/{sid}.mp3"
    out_clip = os.path.join(TEMP_DIR, f"clip_{index:02d}.mp4")
    
    res = subprocess.run(['ffprobe', '-i', audio_path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0'], capture_output=True, text=True)
    duration = float(res.stdout.strip())
    
    total_frames = int(duration * 25)
    
    filter_complex = (
        f"[0:v]scale=1280:720,zoompan=z='min(zoom+0.0003,1.03)':d={total_frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1280x720:fps=25[v]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", img_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "1:a",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-t", str(duration),
        out_clip
    ]
    
    print(f"Rendering video clip {index + 1}/7 ({duration:.2f}s): {out_clip}...")
    subprocess.run(cmd, check=True)
    return out_clip, duration

def generate_ambient_music(total_duration):
    """Generates a soft, upbeat electronic ambient tech background music bed."""
    music_path = os.path.join(TEMP_DIR, "ambient_bed.wav")
    print(f"Synthesizing ambient music bed ({total_duration:.1f}s)...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"aevalsrc="
              f"sin(130.81*2*PI*t)*0.03*sin(2*PI*t/8) + "
              f"sin(164.81*2*PI*t)*0.02*cos(2*PI*t/8) + "
              f"sin(196.00*2*PI*t)*0.02*sin(2*PI*t/8) + "
              f"sin(261.63*2*PI*t)*0.02:s=44100:d={total_duration}",
        "-af", "lowpass=f=950,volume=0.22",
        music_path
    ]
    subprocess.run(cmd, check=True)
    return music_path

def stitch_final_video(clips, total_duration, music_path):
    """Concatenates all clips, mixes background music, and exports the final MP4."""
    concat_list_file = os.path.join(TEMP_DIR, "concat_list.txt")
    with open(concat_list_file, "w") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
            
    raw_concat = os.path.join(TEMP_DIR, "raw_concat.mp4")
    print("Concatenating video segments...")
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        raw_concat
    ], check=True)
    
    print("Mixing voiceover with ambient background music into final MP4...")
    cmd = [
        "ffmpeg", "-y",
        "-i", raw_concat,
        "-i", music_path,
        "-filter_complex",
        "[0:a]volume=1.0[v_audio];"
        "[1:a]volume=0.18,afade=t=out:st=" + str(total_duration - 2) + ":d=2[bg_music];"
        "[v_audio][bg_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "0:v", "-map", "[a_out]",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        FINAL_VIDEO
    ]
    subprocess.run(cmd, check=True)
    print(f"🎉 Final video successfully exported to: {FINAL_VIDEO}")

def main():
    print("=== PassMaster AI Video Walkthrough & Ad Builder ===")
    print("Step 1: Generating slide graphics...")
    render_all_scene_images()
    
    print("Step 2: Rendering video clips with Ken Burns camera motion...")
    clips = []
    total_dur = 0.0
    for idx, sc in enumerate(SCENES):
        clip_path, dur = generate_scene_video(sc, idx)
        clips.append(clip_path)
        total_dur += dur
        
    print(f"Total video duration: {total_dur:.2f} seconds ({total_dur/60:.2f} mins).")
    
    print("Step 3: Creating ambient music bed...")
    music_path = generate_ambient_music(total_dur)
    
    print("Step 4: Assembling final commercial...")
    stitch_final_video(clips, total_dur, music_path)
    
    fsize = os.path.getsize(FINAL_VIDEO) / (1024 * 1024)
    print(f"✓ Video size: {fsize:.2f} MB")
    print("Done!")

if __name__ == "__main__":
    main()

# 🎯 PassMaster AI — Socratic JAMB & WAEC Exam Coach

> **The Next-Gen Exam Mastery Engine for Nigerian & African Students.**
> Stop memorizing past questions. Master underlying concepts, identify leaky topics, and hit 280+ in JAMB with 24/7 Socratic AI coaching.

---

## 💡 Why This Beats Existing Apps
1. **Socratic Error Analysis**: Unlike TestDriller or Myschool which give a 1-sentence static answer, PassMaster AI detects *why* the student failed, identifies the cognitive trap, and coaches them step-by-step.
2. **Leaky Bucket Diagnostics**: Identifies the exact micro-topics (e.g. *Rule of Proximity*, *Gas Laws in Kelvin*, *Chain Rule*) where the student is bleeding JAMB marks.
3. **JAMB Score Predictor**: Dynamic Bayesian prediction of the candidate's actual score out of 400.
4. **WhatsApp Learning Bot**: Zero high-speed data barrier—students can learn, practice, and get coached directly on WhatsApp using cheap daily social data.
5. **Monetization Built-In**: Paystack & Monnify virtual accounts + 12-digit Voucher scratch-card PIN redemption for tutorial centers and offline resellers.

---

## 🚀 Quickstart

### 1. Run Locally
```bash
python3 app.py
```
Server starts on `http://127.0.0.1:5050`

### 2. Run Integration Tests
```bash
python3 -c "
from app import app
client = app.test_client()
print('Testing root:', client.get('/').status_code)
print('Testing questions:', client.get('/api/questions').status_code)
"
```

---

## 💰 Monetization & Pricing Tiers
- **Weekly Drill Pass (₦700)**: 7 days unlimited AI coaching & micro-drills.
- **Monthly Master Pass (₦2,200)**: 30 days + full CBT mocks + WhatsApp bot.
- **Full Season Guarantee (₦5,000)**: Valid until JAMB day + 250+ score guarantee.

---

## 📦 Project Structure
- `app.py`: Flask REST API & Web Server
- `data/questions.json`: Past question bank with cognitive trap annotations
- `data/syllabus.json`: Official syllabus tree with JAMB mark weights
- `engine/socratic_tutor.py`: Socratic AI Tutor & Cognitive Analysis Engine
- `engine/diagnostics.py`: Leaky Bucket Analyzer & 400-Point Score Predictor
- `payments/payment_service.py`: Paystack/Monnify & Voucher PIN redemption
- `whatsapp/bot.py`: WhatsApp Cloud API & Twilio Webhook Handler
- `static/`: Mobile-first, responsive CSS, JavaScript client SPA, PWA manifest
- `templates/index.html`: Master web application interface

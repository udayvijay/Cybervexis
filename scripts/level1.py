# -*- coding: utf-8 -*-
"""Level 1: Cyber Threats (5 topics x 10 questions = 50 questions)"""

level1_questions = [
  # Topic 1: Weak Password Attack
  {
    "id": "L1_T1_SCH_01",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Which password is the hardest for an attacker to guess?",
    "question_en": "Which password is the hardest for an attacker to guess?",
    "question_hi": "इनमें से कौन सा पासवर्ड किसी हमलावर के लिए अनुमान लगाना सबसे कठिन है?",
    "options": [
      "uday123",
      "password",
      "R7!mQ2#vL9",
      "12345678"
    ],
    "options_en": [
      "uday123",
      "password",
      "R7!mQ2#vL9",
      "12345678"
    ],
    "options_hi": [
      "uday123",
      "password",
      "R7!mQ2#vL9",
      "12345678"
    ],
    "answer": "R7!mQ2#vL9",
    "correctAnswerIndex": 2,
    "explanation": "A complex password with upper/lowercase letters, numbers, and special symbols is hardest to crack.",
    "explanation_en": "A complex password with upper/lowercase letters, numbers, and special symbols is hardest to crack.",
    "explanation_hi": "बड़े और छोटे अक्षरों, संख्याओं और विशेष प्रतीकों वाला जटिल पासवर्ड क्रैक करना सबसे कठिन होता है।"
  },
  {
    "id": "L1_T1_SCH_02",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Why is using the same password for many accounts risky?",
    "question_en": "Why is using the same password for many accounts risky?",
    "question_hi": "कई खातों के लिए एक ही पासवर्ड का उपयोग करना जोखिम भरा क्यों है?",
    "options": [
      "It makes the internet slower",
      "One stolen password could unlock several accounts",
      "It deletes your files",
      "It blocks software updates"
    ],
    "options_en": [
      "It makes the internet slower",
      "One stolen password could unlock several accounts",
      "It deletes your files",
      "It blocks software updates"
    ],
    "options_hi": [
      "यह इंटरनेट को धीमा कर देता है",
      "एक चोरी हुआ पासवर्ड कई खातों को अनलॉक कर सकता है",
      "यह आपकी फ़ाइलों को हटा देता है",
      "यह सॉफ्टवेयर अपडेट को रोकता है"
    ],
    "answer": "One stolen password could unlock several accounts",
    "correctAnswerIndex": 1,
    "explanation": "Credential stuffing attacks allow hackers to compromise all your accounts if you reuse a single password.",
    "explanation_en": "Credential stuffing attacks allow hackers to compromise all your accounts if you reuse a single password.",
    "explanation_hi": "यदि आप एक ही पासवर्ड बार-बार इस्तेमाल करते हैं, तो एक खाता हैक होने पर बाकी सभी खाते भी खतरे में पड़ जाते हैं।"
  },
  {
    "id": "L1_T1_SCH_03",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "A website says your password appeared in a data breach. What should you do?",
    "question_en": "A website says your password appeared in a data breach. What should you do?",
    "question_hi": "एक वेबसाइट बताती है कि आपका पासवर्ड डेटा ब्रीच (डेटा लीक) में उजागर हुआ है। आपको क्या करना चाहिए?",
    "options": [
      "Ignore it forever",
      "Use the same password everywhere",
      "Change that password and any reused versions",
      "Post the password to ask for help"
    ],
    "options_en": [
      "Ignore it forever",
      "Use the same password everywhere",
      "Change that password and any reused versions",
      "Post the password to ask for help"
    ],
    "options_hi": [
      "इसे हमेशा के लिए अनदेखा करें",
      "हर जगह उसी पासवर्ड का उपयोग करें",
      "उस पासवर्ड और उसके सभी दोबारा इस्तेमाल किए गए संस्करणों को बदलें",
      "मदद मांगने के लिए पासवर्ड को सोशल मीडिया पर पोस्ट करें"
    ],
    "answer": "Change that password and any reused versions",
    "correctAnswerIndex": 2,
    "explanation": "If a password is leaked in a breach, change it immediately across all services where it was used.",
    "explanation_en": "If a password is leaked in a breach, change it immediately across all services where it was used.",
    "explanation_hi": "यदि कोई पासवर्ड लीक हो जाता है, तो उसे तुरंत और उन सभी जगहों पर बदलें जहां उसका दोबारा इस्तेमाल किया गया था।"
  },
  {
    "id": "L1_T1_SCH_04",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Which is the safest way to store many different passwords?",
    "question_en": "Which is the safest way to store many different passwords?",
    "question_hi": "कई अलग-अलग पासवर्ड सुरक्षित रखने का सबसे सुरक्षित तरीका कौन सा है?",
    "options": [
      "In a public note",
      "In a trusted password manager",
      "In a social media post",
      "As the same easy password"
    ],
    "options_en": [
      "In a public note",
      "In a trusted password manager",
      "In a social media post",
      "As the same easy password"
    ],
    "options_hi": [
      "किसी सार्वजनिक नोट में",
      "एक भरोसेमंद पासवर्ड मैनेजर (Password Manager) में",
      "सोशल मीडिया पोस्ट में",
      "एक ही आसान पासवर्ड के रूप में"
    ],
    "answer": "In a trusted password manager",
    "correctAnswerIndex": 1,
    "explanation": "Password managers encrypt your unique credentials securely behind a single strong master passphrase.",
    "explanation_en": "Password managers encrypt your unique credentials securely behind a single strong master passphrase.",
    "explanation_hi": "पासवर्ड मैनेजर आपके जटिल पासवर्ड को सुरक्षित एन्क्रिप्शन के साथ स्टोर करते हैं।"
  },
  {
    "id": "L1_T1_SCH_05",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "What does multi-factor authentication add to a password?",
    "question_en": "What does multi-factor authentication add to a password?",
    "question_hi": "मल्टी-फ़ैक्टर ऑथेंटिकेशन (MFA) पासवर्ड में क्या अतिरिक्त जोड़ता है?",
    "options": [
      "A second type of sign-in check",
      "A faster internet connection",
      "More storage space",
      "A public profile"
    ],
    "options_en": [
      "A second type of sign-in check",
      "A faster internet connection",
      "More storage space",
      "A public profile"
    ],
    "options_hi": [
      "साइन-इन सत्यापन का दूसरा सुरक्षा स्तर (जैसे OTP या ऐप प्रॉम्प्ट)",
      "एक तेज़ इंटरनेट कनेक्शन",
      "अधिक स्टोरेज स्पेस",
      "एक सार्वजनिक प्रोफ़ाइल"
    ],
    "answer": "A second type of sign-in check",
    "correctAnswerIndex": 0,
    "explanation": "MFA requires an extra verification step (like an OTP or fingerprint) in addition to a password.",
    "explanation_en": "MFA requires an extra verification step (like an OTP or fingerprint) in addition to a password.",
    "explanation_hi": "MFA पासवर्ड के अलावा एक अतिरिक्त सत्यापन चरण (जैसे OTP या फ़िंगरप्रिंट) जोड़ता है।"
  },
  {
    "id": "L1_T1_SCH_06",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Which is the best example of a passphrase?",
    "question_en": "Which is the best example of a passphrase?",
    "question_hi": "पासफ़्रेज़ (Passphrase) का सबसे अच्छा उदाहरण कौन सा है?",
    "options": [
      "cat",
      "123456",
      "BlueRiver!Trains7Dance",
      "qwerty"
    ],
    "options_en": [
      "cat",
      "123456",
      "BlueRiver!Trains7Dance",
      "qwerty"
    ],
    "options_hi": [
      "cat",
      "123456",
      "BlueRiver!Trains7Dance",
      "qwerty"
    ],
    "answer": "BlueRiver!Trains7Dance",
    "correctAnswerIndex": 2,
    "explanation": "A passphrase combines multiple random words, symbols, and numbers for high entropy and easy recall.",
    "explanation_en": "A passphrase combines multiple random words, symbols, and numbers for high entropy and easy recall.",
    "explanation_hi": "पासफ़्रेज़ कई शब्दों, प्रतीकों और संख्याओं को जोड़कर बनाया जाता है, जिससे यह बहुत मजबूत और याद रखने में आसान होता है।"
  },
  {
    "id": "L1_T1_SCH_07",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "A friend asks to borrow your account password. What should you do?",
    "question_en": "A friend asks to borrow your account password. What should you do?",
    "question_hi": "एक दोस्त आपके खाते का पासवर्ड मांगता है। आपको क्या करना चाहिए?",
    "options": [
      "Share it if they are a friend",
      "Send it in a group chat",
      "Keep it private and use safer sharing options if needed",
      "Write it on the classroom board"
    ],
    "options_en": [
      "Share it if they are a friend",
      "Send it in a group chat",
      "Keep it private and use safer sharing options if needed",
      "Write it on the classroom board"
    ],
    "options_hi": [
      "यदि वे दोस्त हैं तो साझा करें",
      "इसे ग्रुप चैट में भेजें",
      "इसे निजी रखें और ज़रूरत पड़ने पर सुरक्षित शेयरिंग विकल्पों का उपयोग करें",
      "इसे क्लासरूम के बोर्ड पर लिखें"
    ],
    "answer": "Keep it private and use safer sharing options if needed",
    "correctAnswerIndex": 2,
    "explanation": "Passwords should never be shared. Use official delegation or collaboration features instead.",
    "explanation_en": "Passwords should never be shared. Use official delegation or collaboration features instead.",
    "explanation_hi": "पासवर्ड कभी किसी के साथ साझा नहीं करना चाहिए। आवश्यकता पड़ने पर आधिकारिक साझाकरण टूल का उपयोग करें।"
  },
  {
    "id": "L1_T1_SCH_08",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Why should you avoid personal details in a password?",
    "question_en": "Why should you avoid personal details in a password?",
    "question_hi": "आपको पासवर्ड में व्यक्तिगत जानकारी (जैसे नाम या जन्मदिन) डालने से क्यों बचना चाहिए?",
    "options": [
      "They may be easy for others to guess",
      "They damage the keyboard",
      "They stop Wi-Fi working",
      "They make the screen dim"
    ],
    "options_en": [
      "They may be easy for others to guess",
      "They damage the keyboard",
      "They stop Wi-Fi working",
      "They make the screen dim"
    ],
    "options_hi": [
      "दूसरों के लिए उनका अनुमान लगाना आसान हो सकता है",
      "वे कीबोर्ड को नुकसान पहुंचाते हैं",
      "वे वाई-फ़ाई को काम करने से रोकते हैं",
      "वे स्क्रीन को मंद कर देते हैं"
    ],
    "answer": "They may be easy for others to guess",
    "correctAnswerIndex": 0,
    "explanation": "Attackers and acquaintances can easily deduce personal details like birthdays, pets, or names.",
    "explanation_en": "Attackers and acquaintances can easily deduce personal details like birthdays, pets, or names.",
    "explanation_hi": "हमलावर सोशल मीडिया या बातचीत के ज़रिए आपके नाम, जन्मदिन या पालतू जानवरों के नाम का आसानी से अनुमान लगा सकते हैं।"
  },
  {
    "id": "L1_T1_SCH_09",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "Which action helps protect an account after signing in on a shared computer?",
    "question_en": "Which action helps protect an account after signing in on a shared computer?",
    "question_hi": "साझा कंप्यूटर (जैसे स्कूल लैब या कैफे) पर साइन इन करने के बाद खाते की सुरक्षा के लिए क्या करना चाहिए?",
    "options": [
      "Save the password in the browser",
      "Stay signed in",
      "Log out and avoid saving the password",
      "Leave the browser open"
    ],
    "options_en": [
      "Save the password in the browser",
      "Stay signed in",
      "Log out and avoid saving the password",
      "Leave the browser open"
    ],
    "options_hi": [
      "ब्राउज़र में पासवर्ड सेव करें",
      "साइन इन ही रहें",
      "लॉग आउट करें और पासवर्ड सेव न करें",
      "ब्राउज़र को खुला छोड़ दें"
    ],
    "answer": "Log out and avoid saving the password",
    "correctAnswerIndex": 2,
    "explanation": "Always explicitly log out and clear browser credentials when using shared or public workstations.",
    "explanation_en": "Always explicitly log out and clear browser credentials when using shared or public workstations.",
    "explanation_hi": "सार्वजनिक कंप्यूटर का उपयोग करने के बाद हमेशा लॉग आउट करें और पासवर्ड कभी सेव न करें।"
  },
  {
    "id": "L1_T1_SCH_10",
    "level": 1,
    "topic": "Weak Password Attack",
    "topicId": "weak_password_attack",
    "mode": "school",
    "question": "What is a sign of a password-spraying attack?",
    "question_en": "What is a sign of a password-spraying attack?",
    "question_hi": "पासवर्ड-स्प्रेइंग (Password-Spraying) हमले का लक्षण क्या है?",
    "options": [
      "Trying a few common passwords against many accounts",
      "Cleaning a keyboard",
      "Installing a printer",
      "Changing screen brightness"
    ],
    "options_en": [
      "Trying a few common passwords against many accounts",
      "Cleaning a keyboard",
      "Installing a printer",
      "Changing screen brightness"
    ],
    "options_hi": [
      "कई अलग-अलग खातों पर कुछ सामान्य पासवर्ड आज़माना",
      "कीबोर्ड की सफाई करना",
      "प्रिंटर इंस्टॉल करना",
      "स्क्रीन की चमक बदलना"
    ],
    "answer": "Trying a few common passwords against many accounts",
    "correctAnswerIndex": 0,
    "explanation": "Password spraying tests a small set of common passwords across many accounts to bypass account lockouts.",
    "explanation_en": "Password spraying tests a small set of common passwords across many accounts to bypass account lockouts.",
    "explanation_hi": "पासवर्ड स्प्रेइंग में हैकर खाता लॉकआउट से बचने के लिए कई खातों पर सामान्य पासवर्ड का परीक्षण करते हैं।"
  },

  # Topic 2: Phishing Attack
  {
    "id": "L1_T2_SCH_01",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "You receive a message saying your account will close in 10 minutes unless you click a link. What is the safest response?",
    "question_en": "You receive a message saying your account will close in 10 minutes unless you click a link. What is the safest response?",
    "question_hi": "आपको एक संदेश मिलता है कि 10 मिनट में आपका खाता बंद हो जाएगा यदि आपने लिंक पर क्लिक नहीं किया। सबसे सुरक्षित कदम क्या है?",
    "options": [
      "Click quickly",
      "Check the message through the official website or app",
      "Reply with your password",
      "Forward it to everyone"
    ],
    "options_en": [
      "Click quickly",
      "Check the message through the official website or app",
      "Reply with your password",
      "Forward it to everyone"
    ],
    "options_hi": [
      "जल्दी से क्लिक करें",
      "संदेश की पुष्टि आधिकारिक वेबसाइट या ऐप के माध्यम से करें",
      "अपने पासवर्ड के साथ उत्तर दें",
      "इसे सभी को फॉरवर्ड करें"
    ],
    "answer": "Check the message through the official website or app",
    "correctAnswerIndex": 1,
    "explanation": "Phishing scams create false urgency. Always independently verify notifications on official websites.",
    "explanation_en": "Phishing scams create false urgency. Always independently verify notifications on official websites.",
    "explanation_hi": "फ़िशिंग संदेश झूठी जल्दबाजी पैदा करते हैं। हमेशा सीधे आधिकारिक वेबसाइट पर जाकर जांच करें।"
  },
  {
    "id": "L1_T2_SCH_02",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "Which is a common sign of a phishing message?",
    "question_en": "Which is a common sign of a phishing message?",
    "question_hi": "फ़िशिंग संदेश का एक सामान्य लक्षण कौन सा है?",
    "options": [
      "A known teacher speaks to you in person",
      "A suspicious link and urgent request for private details",
      "A school timetable on the noticeboard",
      "A saved offline document"
    ],
    "options_en": [
      "A known teacher speaks to you in person",
      "A suspicious link and urgent request for private details",
      "A school timetable on the noticeboard",
      "A saved offline document"
    ],
    "options_hi": [
      "एक परिचित शिक्षक व्यक्तिगत रूप से आपसे बात करते हैं",
      "एक संदिग्ध लिंक और निजी जानकारी के लिए तत्काल अनुरोध",
      "नोटिस बोर्ड पर स्कूल की समय सारिणी",
      "एक सहेजा गया ऑफ़लाइन दस्तावेज़"
    ],
    "answer": "A suspicious link and urgent request for private details",
    "correctAnswerIndex": 1,
    "explanation": "Phishing typically includes unverified links and urgent demands for passwords, PINs, or credentials.",
    "explanation_en": "Phishing typically includes unverified links and urgent demands for passwords, PINs, or credentials.",
    "explanation_hi": "संदिग्ध लिंक और संवेदनशील व्यक्तिगत जानकारी मांगने का दबाव फ़िशिंग के प्रमुख संकेत हैं।"
  },
  {
    "id": "L1_T2_SCH_03",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "A message appears to come from your bank and asks for your PIN. What should you do?",
    "question_en": "A message appears to come from your bank and asks for your PIN. What should you do?",
    "question_hi": "एक संदेश आपके बैंक से आया हुआ प्रतीत होता है और आपका गुप्त PIN मांगता है। आपको क्या करना चाहिए?",
    "options": [
      "Reply with the PIN",
      "Send half the PIN",
      "Do not share it; contact the bank through an official channel",
      "Click every link in the message"
    ],
    "options_en": [
      "Reply with the PIN",
      "Send half the PIN",
      "Do not share it; contact the bank through an official channel",
      "Click every link in the message"
    ],
    "options_hi": [
      "PIN के साथ उत्तर दें",
      "आधा PIN भेजें",
      "इसे साझा न करें; आधिकारिक माध्यम से बैंक से संपर्क करें",
      "संदेश के प्रत्येक लिंक पर क्लिक करें"
    ],
    "answer": "Do not share it; contact the bank through an official channel",
    "correctAnswerIndex": 2,
    "explanation": "Legitimate banks will never ask for your PIN, OTP, or passwords via text or email.",
    "explanation_en": "Legitimate banks will never ask for your PIN, OTP, or passwords via text or email.",
    "explanation_hi": "असली बैंक कभी भी ईमेल या एसएमएस पर आपका गुप्त PIN या पासवर्ड नहीं मांगते।"
  },
  {
    "id": "L1_T2_SCH_04",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "What is a spoofed email address?",
    "question_en": "What is a spoofed email address?",
    "question_hi": "स्पूफ़्ड (Spoofed) ईमेल पता क्या होता है?",
    "options": [
      "An address made to look like it belongs to someone else",
      "A password saved safely",
      "A school email directory",
      "A computer's screen name"
    ],
    "options_en": [
      "An address made to look like it belongs to someone else",
      "A password saved safely",
      "A school email directory",
      "A computer's screen name"
    ],
    "options_hi": [
      "एक ऐसा पता जिसे इस तरह बनाया गया हो कि वह किसी और का लगे",
      "सुरक्षित रूप से सहेजा गया पासवर्ड",
      "स्कूल की ईमेल डायरेक्टरी",
      "कंप्यूटर का स्क्रीन नाम"
    ],
    "answer": "An address made to look like it belongs to someone else",
    "correctAnswerIndex": 0,
    "explanation": "Email spoofing forges the sender header so the message appears to originate from a trusted entity.",
    "explanation_en": "Email spoofing forges the sender header so the message appears to originate from a trusted entity.",
    "explanation_hi": "ईमेल स्पूफिंग में प्रेषक का पता बदलकर ऐसा दिखाया जाता है मानो यह किसी भरोसेमंद व्यक्ति या संस्था से आया हो।"
  },
  {
    "id": "L1_T2_SCH_05",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "How can you check a link before opening it?",
    "question_en": "How can you check a link before opening it?",
    "question_hi": "किसी लिंक को खोलने से पहले आप उसकी जांच कैसे कर सकते हैं?",
    "options": [
      "Look carefully at the actual web address",
      "Trust the logo only",
      "Assume short links are safe",
      "Check how colourful it is"
    ],
    "options_en": [
      "Look carefully at the actual web address",
      "Trust the logo only",
      "Assume short links are safe",
      "Check how colourful it is"
    ],
    "options_hi": [
      "वास्तविक वेब पते (URL) को ध्यान से देखें",
      "केवल लोगो पर भरोसा करें",
      "मान लें कि छोटे लिंक सुरक्षित हैं",
      "देखें कि वह कितना रंगीन है"
    ],
    "answer": "Look carefully at the actual web address",
    "correctAnswerIndex": 0,
    "explanation": "Hovering over or inspecting the URL reveals the actual destination domain and prevents clicking fake sites.",
    "explanation_en": "Hovering over or inspecting the URL reveals the actual destination domain and prevents clicking fake sites.",
    "explanation_hi": "माउस को लिंक पर ले जाकर या URL का विश्लेषण करके वास्तविक डोमेन की जांच की जा सकती है।"
  },
  {
    "id": "L1_T2_SCH_06",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "What is spear phishing?",
    "question_en": "What is spear phishing?",
    "question_hi": "स्पीयर फ़िशिंग (Spear Phishing) क्या है?",
    "options": [
      "A targeted phishing attempt aimed at a particular person or group",
      "A kind of computer monitor",
      "A safe backup method",
      "A type of keyboard"
    ],
    "options_en": [
      "A targeted phishing attempt aimed at a particular person or group",
      "A kind of computer monitor",
      "A safe backup method",
      "A type of keyboard"
    ],
    "options_hi": [
      "किसी विशिष्ट व्यक्ति या समूह को लक्षित करके किया गया फ़िशिंग हमला",
      "कंप्यूटर मॉनिटर का एक प्रकार",
      "एक सुरक्षित बैकअप विधि",
      "एक प्रकार का कीबोर्ड"
    ],
    "answer": "A targeted phishing attempt aimed at a particular person or group",
    "correctAnswerIndex": 0,
    "explanation": "Spear phishing uses tailored personal information to deceive specific individuals or organizations.",
    "explanation_en": "Spear phishing uses tailored personal information to deceive specific individuals or organizations.",
    "explanation_hi": "स्पीयर फ़िशिंग में हमलावर किसी खास व्यक्ति की व्यक्तिगत जानकारी का इस्तेमाल करके उसे धोखा देने का प्रयास करते हैं।"
  },
  {
    "id": "L1_T2_SCH_07",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "A classmate's account sends you an unusual request for money. What should you do?",
    "question_en": "A classmate's account sends you an unusual request for money. What should you do?",
    "question_hi": "किसी सहपाठी के खाते से अचानक पैसे मांगने का असामान्य अनुरोध आता है। आपको क्या करना चाहिए?",
    "options": [
      "Send money immediately",
      "Verify with the classmate through another method",
      "Share your bank details",
      "Post your PIN in reply"
    ],
    "options_en": [
      "Send money immediately",
      "Verify with the classmate through another method",
      "Share your bank details",
      "Post your PIN in reply"
    ],
    "options_hi": [
      "तुरंत पैसे भेजें",
      "किसी अन्य माध्यम (जैसे फोन कॉल या मिलकर) से सहपाठी से पुष्टि करें",
      "अपने बैंक विवरण साझा करें",
      "जवाब में अपना PIN पोस्ट करें"
    ],
    "answer": "Verify with the classmate through another method",
    "correctAnswerIndex": 1,
    "explanation": "Compromised social accounts frequently impersonate friends. Always verify using a separate trusted channel.",
    "explanation_en": "Compromised social accounts frequently impersonate friends. Always verify using a separate trusted channel.",
    "explanation_hi": "यदि किसी मित्र का खाता हैक हो जाए तो हैकर पैसे मांग सकते हैं। हमेशा फोन कॉल करके पुष्टि करें।"
  },
  {
    "id": "L1_T2_SCH_08",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "Why can a fake login page be dangerous?",
    "question_en": "Why can a fake login page be dangerous?",
    "question_hi": "एक नकली लॉगिन पेज (Fake Login Page) खतरनाक क्यों हो सकता है?",
    "options": [
      "It can collect the username and password you enter",
      "It always repairs your computer",
      "It blocks all advertisements",
      "It makes passwords stronger"
    ],
    "options_en": [
      "It can collect the username and password you enter",
      "It always repairs your computer",
      "It blocks all advertisements",
      "It makes passwords stronger"
    ],
    "options_hi": [
      "यह आपके द्वारा दर्ज किए गए यूज़रनेम और पासवर्ड को चुरा सकता है",
      "यह हमेशा आपके कंप्यूटर की मरम्मत करता है",
      "यह सभी विज्ञापनों को ब्लॉक करता है",
      "यह पासवर्ड को मजबूत बनाता है"
    ],
    "answer": "It can collect the username and password you enter",
    "correctAnswerIndex": 0,
    "explanation": "Fake login portals mimic real sites to harvest entered usernames, passwords, and 2FA tokens.",
    "explanation_en": "Fake login portals mimic real sites to harvest entered usernames, passwords, and 2FA tokens.",
    "explanation_hi": "नकली लॉगिन पेज वास्तविक वेबसाइट की नकल करते हैं ताकि वे आपके क्रेडेंशियल्स चुरा सकें।"
  },
  {
    "id": "L1_T2_SCH_09",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "What should you do after entering your password on a suspected fake website?",
    "question_en": "What should you do after entering your password on a suspected fake website?",
    "question_hi": "किसी संदिग्ध नकली वेबसाइट पर अपना पासवर्ड दर्ज करने के बाद आपको क्या करना चाहिए?",
    "options": [
      "Wait a month",
      "Change it using the official site and tell a trusted adult or IT support",
      "Send the password to friends",
      "Turn up the volume"
    ],
    "options_en": [
      "Wait a month",
      "Change it using the official site and tell a trusted adult or IT support",
      "Send the password to friends",
      "Turn up the volume"
    ],
    "options_hi": [
      "एक महीने तक प्रतीक्षा करें",
      "आधिकारिक साइट से पासवर्ड तुरंत बदलें और किसी विश्वसनीय वयस्क या IT सहायता को बताएं",
      "दोस्तों को पासवर्ड भेजें",
      "आवाज बढ़ाएं"
    ],
    "answer": "Change it using the official site and tell a trusted adult or IT support",
    "correctAnswerIndex": 1,
    "explanation": "Immediately reset your credentials on the official platform and inform security/parents.",
    "explanation_en": "Immediately reset your credentials on the official platform and inform security/parents.",
    "explanation_hi": "तुरंत आधिकारिक पोर्टल पर जाकर अपना पासवर्ड बदलें और अपने शिक्षक या अभिभावक को सूचित करें।"
  },
  {
    "id": "L1_T2_SCH_10",
    "level": 1,
    "topic": "Phishing Attack",
    "topicId": "phishing_attack",
    "mode": "school",
    "question": "Which message is most suspicious?",
    "question_en": "Which message is most suspicious?",
    "question_hi": "इनमें से कौन सा संदेश सबसे अधिक संदिग्ध है?",
    "options": [
      "A normal message from a known contact you expected",
      "A school notice confirmed on the official portal",
      "A prize claim asking for your password and a fee",
      "A saved homework reminder"
    ],
    "options_en": [
      "A normal message from a known contact you expected",
      "A school notice confirmed on the official portal",
      "A prize claim asking for your password and a fee",
      "A saved homework reminder"
    ],
    "options_hi": [
      "किसी परिचित संपर्क से अपेक्षित सामान्य संदेश",
      "आधिकारिक पोर्टल पर पुष्ट किया गया स्कूल नोटिस",
      "एक लॉटरी या इनाम का दावा जिसमें आपका पासवर्ड और शुल्क मांगा गया हो",
      "गृहकार्य का सहेजा गया रिमाइंडर"
    ],
    "answer": "A prize claim asking for your password and a fee",
    "correctAnswerIndex": 2,
    "explanation": "Unsolicited prize notifications requesting money or credentials are classic phishing frauds.",
    "explanation_en": "Unsolicited prize notifications requesting money or credentials are classic phishing frauds.",
    "explanation_hi": "अचानक कोई लॉटरी या पुरस्कार जीतने का दावा करके पासवर्ड या पैसे मांगना फ़िशिंग फ्रॉड होता है।"
  },

  # Topic 3: Malware Infection
  {
    "id": "L1_T3_SCH_01",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "Which best describes malware?",
    "question_en": "Which best describes malware?",
    "question_hi": "मैलवेयर (Malware) का सबसे सटीक वर्णन कौन सा है?",
    "options": [
      "Software designed to harm, disrupt, or misuse a device",
      "A tool for cleaning a screen",
      "A normal school timetable",
      "A type of computer desk"
    ],
    "options_en": [
      "Software designed to harm, disrupt, or misuse a device",
      "A tool for cleaning a screen",
      "A normal school timetable",
      "A type of computer desk"
    ],
    "options_hi": [
      "कंप्यूटर या डिवाइस को नुकसान पहुंचाने, बाधित करने या दुरुपयोग करने के लिए बनाया गया सॉफ्टवेयर",
      "स्क्रीन साफ करने का एक टूल",
      "एक सामान्य स्कूल समय सारिणी",
      "एक प्रकार की कंप्यूटर डेस्क"
    ],
    "answer": "Software designed to harm, disrupt, or misuse a device",
    "correctAnswerIndex": 0,
    "explanation": "Malware is malicious software written specifically to compromise, steal from, or damage devices.",
    "explanation_en": "Malware is malicious software written specifically to compromise, steal from, or damage devices.",
    "explanation_hi": "मैलवेयर दुर्भावनापूर्ण सॉफ्टवेयर होता है जो सिस्टम को नुकसान पहुंचाने या डेटा चुराने के लिए बनाया जाता है।"
  },
  {
    "id": "L1_T3_SCH_02",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "What is ransomware commonly designed to do?",
    "question_en": "What is ransomware commonly designed to do?",
    "question_hi": "रैनसमवेयर (Ransomware) आमतौर पर क्या करने के लिए डिज़ाइन किया जाता है?",
    "options": [
      "Lock or encrypt files and demand payment",
      "Improve battery life",
      "Make a stronger password",
      "Organize photos safely"
    ],
    "options_en": [
      "Lock or encrypt files and demand payment",
      "Improve battery life",
      "Make a stronger password",
      "Organize photos safely"
    ],
    "options_hi": [
      "फ़ाइलों को लॉक या एन्क्रिप्ट करना और फिरौती (भुगतान) की मांग करना",
      "बैटरी जीवन में सुधार करना",
      "एक मजबूत पासवर्ड बनाना",
      "तस्वीरों को सुरक्षित रूप से व्यवस्थित करना"
    ],
    "answer": "Lock or encrypt files and demand payment",
    "correctAnswerIndex": 0,
    "explanation": "Ransomware locks your system or files with strong encryption and demands ransom money for decryption.",
    "explanation_en": "Ransomware locks your system or files with strong encryption and demands ransom money for decryption.",
    "explanation_hi": "रैनसमवेयर उपयोगकर्ता की फ़ाइलों को एन्क्रिप्ट करके लॉक कर देता है और उन्हें खोलने के लिए फिरौती मांगता है।"
  },
  {
    "id": "L1_T3_SCH_03",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "Which download is safest?",
    "question_en": "Which download is safest?",
    "question_hi": "इनमें से कौन सा डाउनलोड सबसे सुरक्षित है?",
    "options": [
      "A cracked game from an unknown site",
      "An attachment from a stranger",
      "An app from an official or trusted source",
      "A file advertised by a pop-up"
    ],
    "options_en": [
      "A cracked game from an unknown site",
      "An attachment from a stranger",
      "An app from an official or trusted source",
      "A file advertised by a pop-up"
    ],
    "options_hi": [
      "किसी अनजान वेबसाइट से क्रैक किया गया गेम",
      "किसी अजनबी से ईमेल में मिला अटैचमेंट",
      "आधिकारिक या विश्वसनीय ऐप स्टोर से डाउनलोड किया गया ऐप",
      "पॉप-अप विज्ञापन द्वारा प्रचारित फ़ाइल"
    ],
    "answer": "An app from an official or trusted source",
    "correctAnswerIndex": 2,
    "explanation": "Always download applications from vetted, official app stores and verified developers.",
    "explanation_en": "Always download applications from vetted, official app stores and verified developers.",
    "explanation_hi": "हमेशा आधिकारिक ऐप स्टोर या विश्वसनीय डेवलपर से ही सॉफ्टवेयर डाउनलोड करना चाहिए।"
  },
  {
    "id": "L1_T3_SCH_04",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "Why should you keep security software updated?",
    "question_en": "Why should you keep security software updated?",
    "question_hi": "आपको सुरक्षा सॉफ़्टवेयर (Antivirus) को हमेशा अपडेट क्यों रखना चाहिए?",
    "options": [
      "It can recognize newer threats and fix weaknesses",
      "It makes every email genuine",
      "It removes the need for backups",
      "It prevents all mistakes"
    ],
    "options_en": [
      "It can recognize newer threats and fix weaknesses",
      "It makes every email genuine",
      "It removes the need for backups",
      "It prevents all mistakes"
    ],
    "options_hi": [
      "यह नए खतरों की पहचान कर सकता है और सुरक्षा खामियों को ठीक कर सकता है",
      "यह हर ईमेल को असली बना देता है",
      "यह बैकअप की आवश्यकता को समाप्त कर देता है",
      "यह सभी मानवीय गलतियों को रोकता है"
    ],
    "answer": "It can recognize newer threats and fix weaknesses",
    "correctAnswerIndex": 0,
    "explanation": "Updates provide the latest virus definitions and security patches against newly engineered exploits.",
    "explanation_en": "Updates provide the latest virus definitions and security patches against newly engineered exploits.",
    "explanation_hi": "अपडेट से एंटीवायरस को नए वायरस और मैलवेयर के बारे में जानकारी मिलती है जिससे वह उनसे रक्षा कर पाता है।"
  },
  {
    "id": "L1_T3_SCH_05",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "A computer suddenly shows many strange pop-ups after installing a file. What should you do?",
    "question_en": "A computer suddenly shows many strange pop-ups after installing a file. What should you do?",
    "question_hi": "किसी फ़ाइल को इंस्टॉल करने के बाद कंप्यूटर पर अचानक कई अजीब पॉप-अप दिखने लगते हैं। आपको क्या करना चाहिए?",
    "options": [
      "Install more unknown files",
      "Tell a trusted adult or IT support and run a trusted security check",
      "Enter your passwords into the pop-ups",
      "Ignore every warning"
    ],
    "options_en": [
      "Install more unknown files",
      "Tell a trusted adult or IT support and run a trusted security check",
      "Enter your passwords into the pop-ups",
      "Ignore every warning"
    ],
    "options_hi": [
      "और अज्ञात फ़ाइलें इंस्टॉल करें",
      "किसी विश्वसनीय वयस्क या IT सहायता को बताएं और एंटीवायरस स्कैन चलाएं",
      "पॉप-अप में अपने पासवर्ड दर्ज करें",
      "हर चेतावनी को नज़रअंदाज़ करें"
    ],
    "answer": "Tell a trusted adult or IT support and run a trusted security check",
    "correctAnswerIndex": 1,
    "explanation": "Sudden pop-ups suggest adware or malware. Isolate the device and run a full antivirus scan.",
    "explanation_en": "Sudden pop-ups suggest adware or malware. Isolate the device and run a full antivirus scan.",
    "explanation_hi": "अचानक अनचाहे पॉप-अप आना मैलवेयर का लक्षण है। तुरंत एंटीवायरस से सिस्टम स्कैन करें।"
  },
  {
    "id": "L1_T3_SCH_06",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "What is spyware designed to do?",
    "question_en": "What is spyware designed to do?",
    "question_hi": "स्पायवेयर (Spyware) क्या करने के लिए डिज़ाइन किया गया है?",
    "options": [
      "Secretly collect information about a user or device",
      "Protect files with a backup",
      "Cool a laptop",
      "Improve typing speed"
    ],
    "options_en": [
      "Secretly collect information about a user or device",
      "Protect files with a backup",
      "Cool a laptop",
      "Improve typing speed"
    ],
    "options_hi": [
      "उपयोगकर्ता या डिवाइस की जानकारी चुपके से एकत्र करना",
      "बैकअप के साथ फ़ाइलों को सुरक्षित रखना",
      "लैपटॉप को ठंडा रखना",
      "टाइपिंग की गति में सुधार करना"
    ],
    "answer": "Secretly collect information about a user or device",
    "correctAnswerIndex": 0,
    "explanation": "Spyware covertly tracks keystrokes, browsing habits, and credentials without user consent.",
    "explanation_en": "Spyware covertly tracks keystrokes, browsing habits, and credentials without user consent.",
    "explanation_hi": "स्पायवेयर उपयोगकर्ता की जानकारी और गतिविधियों की जासूसी करके उन्हें हमलावर तक भेजता है।"
  },
  {
    "id": "L1_T3_SCH_07",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "How can a USB drive spread malware?",
    "question_en": "How can a USB drive spread malware?",
    "question_hi": "एक USB ड्राइव (पेन ड्राइव) मैलवेयर कैसे फैला सकती है?",
    "options": [
      "An infected file on it may be opened or run",
      "It always changes the screen colour",
      "It increases internet speed",
      "It automatically creates a strong password"
    ],
    "options_en": [
      "An infected file on it may be opened or run",
      "It always changes the screen colour",
      "It increases internet speed",
      "It automatically creates a strong password"
    ],
    "options_hi": [
      "उस पर मौजूद संक्रमित फ़ाइल खोली या चलाई जा सकती है",
      "यह हमेशा स्क्रीन का रंग बदल देती है",
      "यह इंटरनेट की गति बढ़ा देती है",
      "यह स्वचालित रूप से एक मजबूत पासवर्ड बनाती है"
    ],
    "answer": "An infected file on it may be opened or run",
    "correctAnswerIndex": 0,
    "explanation": "Opening compromised executables or autorun scripts on USB drives can infect the host system.",
    "explanation_en": "Opening compromised executables or autorun scripts on USB drives can infect the host system.",
    "explanation_hi": "USB ड्राइव में मौजूद वायरस वाली फ़ाइल को खोलने से वह वायरस कंप्यूटर में फैल जाता है।"
  },
  {
    "id": "L1_T3_SCH_08",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "Which practice lowers the risk of malware infection?",
    "question_en": "Which practice lowers the risk of malware infection?",
    "question_hi": "इनमें से कौन सा अभ्यास मैलवेयर संक्रमण के जोखिम को कम करता है?",
    "options": [
      "Opening unknown attachments",
      "Disabling all updates",
      "Installing updates and avoiding suspicious downloads",
      "Sharing administrator access"
    ],
    "options_en": [
      "Opening unknown attachments",
      "Disabling all updates",
      "Installing updates and avoiding suspicious downloads",
      "Sharing administrator access"
    ],
    "options_hi": [
      "अज्ञात ईमेल अटैचमेंट खोलना",
      "सभी अपडेट को अक्षम करना",
      "अपडेट इंस्टॉल करना और संदिग्ध डाउनलोड से बचना",
      "व्यवस्थापक (Admin) एक्सेस साझा करना"
    ],
    "answer": "Installing updates and avoiding suspicious downloads",
    "correctAnswerIndex": 2,
    "explanation": "Regular patching and downloading exclusively from trusted sources prevents infections.",
    "explanation_en": "Regular patching and downloading exclusively from trusted sources prevents infections.",
    "explanation_hi": "सिस्टम को नियमित अपडेट रखना और संदिग्ध साइटों से डाउनलोड न करना आपको सुरक्षित रखता है।"
  },
  {
    "id": "L1_T3_SCH_09",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "Why are pirated applications risky?",
    "question_en": "Why are pirated applications risky?",
    "question_hi": "पायरेटेड (Pirated/Cracked) एप्लिकेशन जोखिम भरी क्यों होती हैं?",
    "options": [
      "They may contain hidden malware and lack trusted updates",
      "They always use less storage",
      "They cannot access files",
      "They are always checked by the maker"
    ],
    "options_en": [
      "They may contain hidden malware and lack trusted updates",
      "They always use less storage",
      "They cannot access files",
      "They are always checked by the maker"
    ],
    "options_hi": [
      "वे छिपे हुए मैलवेयर ले जा सकती हैं और उनमें आधिकारिक सुरक्षा अपडेट नहीं होते",
      "वे हमेशा कम स्टोरेज का उपयोग करती हैं",
      "वे फ़ाइलों तक पहुँच नहीं सकती हैं",
      "उन्हें हमेशा मूल निर्माता द्वारा जाँचा जाता है"
    ],
    "answer": "They may contain hidden malware and lack trusted updates",
    "correctAnswerIndex": 0,
    "explanation": "Cracked software frequently bundles trojans, spyware, and backdoors designed to hijack your device.",
    "explanation_en": "Cracked software frequently bundles trojans, spyware, and backdoors designed to hijack your device.",
    "explanation_hi": "पायरेटेड गेम्स और सॉफ्टवेयर में अक्सर ट्रोजन और मैलवेयर छिपे होते हैं जो कंप्यूटर को हैक कर लेते हैं।"
  },
  {
    "id": "L1_T3_SCH_10",
    "level": 1,
    "topic": "Malware Infection",
    "topicId": "malware_infection",
    "mode": "school",
    "question": "What is one reason to keep a backup separate from your main device?",
    "question_en": "What is one reason to keep a backup separate from your main device?",
    "question_hi": "अपने मुख्य डिवाइस से अलग एक बैकअप रखने का एक मुख्य कारण क्या है?",
    "options": [
      "Malware or device failure may affect the original files",
      "It makes phishing impossible",
      "It removes every virus automatically",
      "It makes Wi-Fi private"
    ],
    "options_en": [
      "Malware or device failure may affect the original files",
      "It makes phishing impossible",
      "It removes every virus automatically",
      "It makes Wi-Fi private"
    ],
    "options_hi": [
      "मैलवेयर या हार्डवेयर खराबी मूल फ़ाइलों को नष्ट कर सकती है",
      "यह फ़िशिंग को असंभव बनाता है",
      "यह हर वायरस को अपने आप हटा देता है",
      "यह वाई-फ़ाई को निजी बना देता है"
    ],
    "answer": "Malware or device failure may affect the original files",
    "correctAnswerIndex": 0,
    "explanation": "Offline/isolated backups ensure data recovery even if the primary machine suffers ransomware or crash.",
    "explanation_en": "Offline/isolated backups ensure data recovery even if the primary machine suffers ransomware or crash.",
    "explanation_hi": "यदि मुख्य कंप्यूटर पर रैनसमवेयर हमला हो जाए या हार्ड डिस्क खराब हो जाए, तो अलग बैकअप से डेटा वापस मिल जाता है।"
  },

  # Topic 4: Unsafe Public Wi-Fi
  {
    "id": "L1_T4_SCH_01",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "Why can an unknown public Wi-Fi network be risky?",
    "question_en": "Why can an unknown public Wi-Fi network be risky?",
    "question_hi": "एक अज्ञात सार्वजनिक वाई-फ़ाई (Public Wi-Fi) नेटवर्क जोखिम भरा क्यों हो सकता है?",
    "options": [
      "Someone may operate a fake network or monitor poorly protected traffic",
      "It always breaks the keyboard",
      "It makes passwords longer",
      "It automatically deletes photos"
    ],
    "options_en": [
      "Someone may operate a fake network or monitor poorly protected traffic",
      "It always breaks the keyboard",
      "It makes passwords longer",
      "It automatically deletes photos"
    ],
    "options_hi": [
      "कोई फर्जी नेटवर्क चला सकता है या असुरक्षित डेटा ट्रैफिक की जासूसी कर सकता है",
      "यह हमेशा कीबोर्ड को तोड़ देता है",
      "यह पासवर्ड को लंबा कर देता है",
      "यह स्वचालित रूप से तस्वीरों को हटा देता है"
    ],
    "answer": "Someone may operate a fake network or monitor poorly protected traffic",
    "correctAnswerIndex": 0,
    "explanation": "Public Wi-Fi networks lack encryption between clients, allowing attackers to snoop on transmitted data.",
    "explanation_en": "Public Wi-Fi networks lack encryption between clients, allowing attackers to snoop on transmitted data.",
    "explanation_hi": "सार्वजनिक वाई-फ़ाई पर कोई भी हैकर नेटवर्क में बह रहे डेटा को इंटरसेप्ट या मॉनिटर कर सकता है।"
  },
  {
    "id": "L1_T4_SCH_02",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "A café has two Wi-Fi names that look similar. What should you do?",
    "question_en": "A café has two Wi-Fi names that look similar. What should you do?",
    "question_hi": "एक कैफे में दो समान दिखने वाले वाई-फ़ाई नाम हैं। आपको क्या करना चाहिए?",
    "options": [
      "Join the one with the strongest signal without checking",
      "Ask staff for the official network name",
      "Use both at once",
      "Choose the one with no password every time"
    ],
    "options_en": [
      "Join the one with the strongest signal without checking",
      "Ask staff for the official network name",
      "Use both at once",
      "Choose the one with no password every time"
    ],
    "options_hi": [
      "बिना जांचे सबसे मजबूत सिग्नल वाले से जुड़ें",
      "कर्मचारियों से आधिकारिक नेटवर्क का सही नाम पूछें",
      "एक साथ दोनों का उपयोग करें",
      "हर बार बिना पासवर्ड वाले को चुनें"
    ],
    "answer": "Ask staff for the official network name",
    "correctAnswerIndex": 1,
    "explanation": "Attackers set up rogue 'Evil Twin' access points with similar names to trick visitors into connecting.",
    "explanation_en": "Attackers set up rogue 'Evil Twin' access points with similar names to trick visitors into connecting.",
    "explanation_hi": "हमलावर नकली वाई-फ़ाई हॉटस्पॉट बनाते हैं। इसलिए कैफ़े के कर्मचारियों से असली नेटवर्क का नाम पूछना चाहिए।"
  },
  {
    "id": "L1_T4_SCH_03",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "Which activity is best avoided on an untrusted public Wi-Fi network?",
    "question_en": "Which activity is best avoided on an untrusted public Wi-Fi network?",
    "question_hi": "अविश्वसनीय सार्वजनिक वाई-फ़ाई पर किस गतिविधि से बचना सबसे अच्छा है?",
    "options": [
      "Reading a public news page",
      "Checking the weather",
      "Accessing sensitive accounts without suitable protection",
      "Reading an offline document"
    ],
    "options_en": [
      "Reading a public news page",
      "Checking the weather",
      "Accessing sensitive accounts without suitable protection",
      "Reading an offline document"
    ],
    "options_hi": [
      "सार्वजनिक समाचार पढ़ना",
      "मौसम की जानकारी देखना",
      "उचित सुरक्षा के बिना संवेदनशील बैंक या व्यक्तिगत खातों को खोलना",
      "ऑफ़लाइन दस्तावेज़ पढ़ना"
    ],
    "answer": "Accessing sensitive accounts without suitable protection",
    "correctAnswerIndex": 2,
    "explanation": "Avoid online banking or accessing sensitive portals on unsecured networks unless using a trusted VPN.",
    "explanation_en": "Avoid online banking or accessing sensitive portals on unsecured networks unless using a trusted VPN.",
    "explanation_hi": "असुरक्षित वाई-फ़ाई पर बैंकिंग या संवेदनशील खातों में लॉगिन करने से क्रेडेंशियल चोरी हो सकते हैं।"
  },
  {
    "id": "L1_T4_SCH_04",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "What does HTTPS generally help protect?",
    "question_en": "What does HTTPS generally help protect?",
    "question_hi": "HTTPS आम तौर पर किसकी सुरक्षा में मदद करता है?",
    "options": [
      "Data sent between your browser and the website through encryption",
      "Your device from every possible virus",
      "Your account from weak passwords",
      "Your files from being deleted"
    ],
    "options_en": [
      "Data sent between your browser and the website through encryption",
      "Your device from every possible virus",
      "Your account from weak passwords",
      "Your files from being deleted"
    ],
    "options_hi": [
      "एन्क्रिप्शन के माध्यम से आपके ब्राउज़र और वेबसाइट के बीच भेजे गए डेटा की सुरक्षा",
      "आपके डिवाइस को हर संभावित वायरस से बचाना",
      "कमजोर पासवर्ड से आपके खाते की सुरक्षा",
      "आपकी फ़ाइलों को डिलीट होने से बचाना"
    ],
    "answer": "Data sent between your browser and the website through encryption",
    "correctAnswerIndex": 0,
    "explanation": "HTTPS encrypts the communication channel between your web browser and the server.",
    "explanation_en": "HTTPS encrypts the communication channel between your web browser and the server.",
    "explanation_hi": "HTTPS आपके ब्राउज़र और सर्वर के बीच संचार को एन्क्रिप्ट करता है जिससे बीच में कोई इसे पढ़ नहीं सकता।"
  },
  {
    "id": "L1_T4_SCH_05",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "Does a VPN make every online action completely safe?",
    "question_en": "Does a VPN make every online action completely safe?",
    "question_hi": "क्या VPN ऑनलाइन की जाने वाली हर गतिविधि को पूरी तरह से सुरक्षित बना देता है?",
    "options": [
      "Yes, always",
      "No; it can protect some traffic but other risks remain",
      "Only when the screen is bright",
      "Only for games"
    ],
    "options_en": [
      "Yes, always",
      "No; it can protect some traffic but other risks remain",
      "Only when the screen is bright",
      "Only for games"
    ],
    "options_hi": [
      "हाँ, हमेशा",
      "नहीं; यह नेटवर्क डेटा को सुरक्षित करता है लेकिन मैलवेयर और फ़िशिंग जैसे अन्य जोखिम बने रहते हैं",
      "केवल जब स्क्रीन चमकदार हो",
      "केवल गेम्स के लिए"
    ],
    "answer": "No; it can protect some traffic but other risks remain",
    "correctAnswerIndex": 1,
    "explanation": "A VPN encrypts network transit, but it does not protect against malware, phishing, or giving away passwords.",
    "explanation_en": "A VPN encrypts network transit, but it does not protect against malware, phishing, or giving away passwords.",
    "explanation_hi": "VPN केवल नेटवर्क ट्रैफ़िक को एन्क्रिप्ट करता है; यदि आप फ़िशिंग साइट पर पासवर्ड डालते हैं तो VPN उससे नहीं बचा सकता।"
  },
  {
    "id": "L1_T4_SCH_06",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "What is a possible danger of a fake Wi-Fi hotspot?",
    "question_en": "What is a possible danger of a fake Wi-Fi hotspot?",
    "question_hi": "एक नकली वाई-फ़ाई हॉटस्पॉट का संभावित खतरा क्या है?",
    "options": [
      "It may trick users into connecting to an attacker's network",
      "It always improves privacy",
      "It creates backups",
      "It fixes software bugs"
    ],
    "options_en": [
      "It may trick users into connecting to an attacker's network",
      "It always improves privacy",
      "It creates backups",
      "It fixes software bugs"
    ],
    "options_hi": [
      "यह उपयोगकर्ताओं को हमलावर के नेटवर्क से जोड़ने के लिए धोखा दे सकता है",
      "यह हमेशा गोपनीयता में सुधार करता है",
      "यह बैकअप बनाता है",
      "यह सॉफ़्टवेयर बग्स को ठीक करता है"
    ],
    "answer": "It may trick users into connecting to an attacker's network",
    "correctAnswerIndex": 0,
    "explanation": "Rogue hotspots can perform Man-in-the-Middle (MitM) attacks and monitor unencrypted credentials.",
    "explanation_en": "Rogue hotspots can perform Man-in-the-Middle (MitM) attacks and monitor unencrypted credentials.",
    "explanation_hi": "नकली हॉटस्पॉट से कनेक्ट होने पर हैकर आपके इंटरनेट ट्रैफ़िक और लॉगिन क्रेडेंशियल्स की निगरानी कर सकते हैं।"
  },
  {
    "id": "L1_T4_SCH_07",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "What should you do after using your account on a shared computer?",
    "question_en": "What should you do after using your account on a shared computer?",
    "question_hi": "साझा कंप्यूटर पर अपने खाते का उपयोग करने के बाद आपको क्या करना चाहिए?",
    "options": [
      "Leave it signed in",
      "Save your password for the next person",
      "Log out and close the session",
      "Share the browser history"
    ],
    "options_en": [
      "Leave it signed in",
      "Save your password for the next person",
      "Log out and close the session",
      "Share the browser history"
    ],
    "options_hi": [
      "साइन इन ही छोड़ दें",
      "अगले व्यक्ति के लिए पासवर्ड सेव करें",
      "लॉग आउट करें और सत्र (ब्राउज़र) बंद करें",
      "ब्राउज़र हिस्ट्री साझा करें"
    ],
    "answer": "Log out and close the session",
    "correctAnswerIndex": 2,
    "explanation": "Logging out and closing the session prevents subsequent users from hijacking your account session.",
    "explanation_en": "Logging out and closing the session prevents subsequent users from hijacking your account session.",
    "explanation_hi": "लॉग आउट करने और ब्राउज़र बंद करने से अगला उपयोगकर्ता आपके खाते का गलत इस्तेमाल नहीं कर सकता।"
  },
  {
    "id": "L1_T4_SCH_08",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "Which setting is safer on public Wi-Fi?",
    "question_en": "Which setting is safer on public Wi-Fi?",
    "question_hi": "सार्वजनिक वाई-फ़ाई पर कौन सी सेटिंग अधिक सुरक्षित है?",
    "options": [
      "Allow everyone to access shared folders",
      "Turn off unnecessary file sharing",
      "Accept every certificate warning",
      "Use the same password everywhere"
    ],
    "options_en": [
      "Allow everyone to access shared folders",
      "Turn off unnecessary file sharing",
      "Accept every certificate warning",
      "Use the same password everywhere"
    ],
    "options_hi": [
      "सभी को साझा फ़ोल्डरों तक पहुँचने की अनुमति दें",
      "अनावश्यक फ़ाइल शेयरिंग (File Sharing) को बंद रखें",
      "प्रत्येक प्रमाणपत्र चेतावनी को स्वीकार करें",
      "हर जगह एक ही पासवर्ड का उपयोग करें"
    ],
    "answer": "Turn off unnecessary file sharing",
    "correctAnswerIndex": 1,
    "explanation": "Disabling file and network sharing prevents unauthorized local devices from accessing your shared folders.",
    "explanation_en": "Disabling file and network sharing prevents unauthorized local devices from accessing your shared folders.",
    "explanation_hi": "फ़ाइल शेयरिंग बंद रखने से उसी वाई-फ़ाई से जुड़े अन्य लोग आपके कंप्यूटर की फ़ाइलों तक नहीं पहुँच सकते।"
  },
  {
    "id": "L1_T4_SCH_09",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "Why should you avoid ignoring browser security warnings?",
    "question_en": "Why should you avoid ignoring browser security warnings?",
    "question_hi": "आपको ब्राउज़र सुरक्षा चेतावनियों को नज़रअंदाज़ करने से क्यों बचना चाहिए?",
    "options": [
      "They may indicate a problem with the connection or website certificate",
      "They mean the website is always safe",
      "They improve Wi-Fi speed",
      "They are only decorations"
    ],
    "options_en": [
      "They may indicate a problem with the connection or website certificate",
      "They mean the website is always safe",
      "They improve Wi-Fi speed",
      "They are only decorations"
    ],
    "options_hi": [
      "वे कनेक्शन या वेबसाइट प्रमाणपत्र में किसी समस्या या जासूसी का संकेत हो सकते हैं",
      "उनका अर्थ है कि वेबसाइट हमेशा सुरक्षित है",
      "वे वाई-फ़ाई की गति बढ़ाते हैं",
      "वे केवल सजावट के लिए हैं"
    ],
    "answer": "They may indicate a problem with the connection or website certificate",
    "correctAnswerIndex": 0,
    "explanation": "Certificate errors often indicate interception attacks or expired/forged credentials on the website.",
    "explanation_en": "Certificate errors often indicate interception attacks or expired/forged credentials on the website.",
    "explanation_hi": "सर्टिफिकेट चेतावनी यह दर्शाती है कि कनेक्शन सुरक्षित नहीं है या कोई आपके डेटा को चुराने की कोशिश कर रहा है।"
  },
  {
    "id": "L1_T4_SCH_10",
    "level": 1,
    "topic": "Unsafe Public Wi-Fi",
    "topicId": "unsafe_public_wifi",
    "mode": "school",
    "question": "If you must use a sensitive service while travelling, what is best?",
    "question_en": "If you must use a sensitive service while travelling, what is best?",
    "question_hi": "यदि यात्रा के दौरान आपको किसी संवेदनशील सेवा का उपयोग करना पड़े, तो सबसे अच्छा क्या है?",
    "options": [
      "Use a trusted connection and the official app or website",
      "Use any open network and ignore warnings",
      "Share the login with a stranger",
      "Turn off all account security"
    ],
    "options_en": [
      "Use a trusted connection and the official app or website",
      "Use any open network and ignore warnings",
      "Share the login with a stranger",
      "Turn off all account security"
    ],
    "options_hi": [
      "भरोसेमंद कनेक्शन (जैसे मोबाइल डेटा) और आधिकारिक ऐप या वेबसाइट का उपयोग करें",
      "किसी भी खुले नेटवर्क का उपयोग करें और चेतावनियों को अनदेखा करें",
      "किसी अजनबी के साथ लॉगिन साझा करें",
      "सभी खाता सुरक्षा बंद कर दें"
    ],
    "answer": "Use a trusted connection and the official app or website",
    "correctAnswerIndex": 0,
    "explanation": "Use cellular data or an encrypted VPN rather than open public Wi-Fi for sensitive transactions.",
    "explanation_en": "Use cellular data or an encrypted VPN rather than open public Wi-Fi for sensitive transactions.",
    "explanation_hi": "यात्रा करते समय खुले वाई-फ़ाई के बजाय अपने मोबाइल डेटा या वीपीएन का उपयोग करना सुरक्षित रहता है।"
  },

  # Topic 5: Data Leak
  {
    "id": "L1_T5_SCH_01",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "What is a data leak?",
    "question_en": "What is a data leak?",
    "question_hi": "डेटा लीक (Data Leak) क्या होता है?",
    "options": [
      "Private or sensitive information being exposed to people who should not access it",
      "A computer running out of battery",
      "A keyboard key getting stuck",
      "A slow internet connection"
    ],
    "options_en": [
      "Private or sensitive information being exposed to people who should not access it",
      "A computer running out of battery",
      "A keyboard key getting stuck",
      "A slow internet connection"
    ],
    "options_hi": [
      "निजी या संवेदनशील जानकारी का उन लोगों के सामने उजागर होना जिन्हें इसकी अनुमति नहीं होनी चाहिए",
      "कंप्यूटर की बैटरी खत्म होना",
      "कीबोर्ड की कुंजी का अटक जाना",
      "धीमा इंटरनेट कनेक्शन"
    ],
    "answer": "Private or sensitive information being exposed to people who should not access it",
    "correctAnswerIndex": 0,
    "explanation": "A data leak is the unauthorized transmission or exposure of confidential information to untrusted parties.",
    "explanation_en": "A data leak is the unauthorized transmission or exposure of confidential information to untrusted parties.",
    "explanation_hi": "डेटा लीक का अर्थ है गोपनीय या व्यक्तिगत जानकारी का अनधिकृत व्यक्तियों के सामने सार्वजनिक या उजागर हो जाना।"
  },
  {
    "id": "L1_T5_SCH_02",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "A student accidentally sends a file containing classmates' phone numbers to the wrong group. What should they do?",
    "question_en": "A student accidentally sends a file containing classmates' phone numbers to the wrong group. What should they do?",
    "question_hi": "एक छात्र गलती से सहपाठियों के फोन नंबर वाली फ़ाइल किसी गलत ग्रुप में भेज देता है। उसे क्या करना चाहिए?",
    "options": [
      "Ignore it",
      "Report it quickly and follow instructions to limit sharing",
      "Send it to more groups",
      "Post it publicly"
    ],
    "options_en": [
      "Ignore it",
      "Report it quickly and follow instructions to limit sharing",
      "Send it to more groups",
      "Post it publicly"
    ],
    "options_hi": [
      "इसे नज़रअंदाज़ करें",
      "इसकी तुरंत सूचना दें और आगे फैलने से रोकने के निर्देशों का पालन करें",
      "इसे और समूहों में भेजें",
      "इसे सार्वजनिक रूप से पोस्ट करें"
    ],
    "answer": "Report it quickly and follow instructions to limit sharing",
    "correctAnswerIndex": 1,
    "explanation": "Prompt reporting allows administrators to contain the breach, delete copies, and notify affected parties.",
    "explanation_en": "Prompt reporting allows administrators to contain the breach, delete copies, and notify affected parties.",
    "explanation_hi": "गलती से संवेदनशील डेटा साझा होने पर तुरंत शिक्षक या व्यवस्थापक को बताना चाहिए ताकि नुकसान कम किया जा सके।"
  },
  {
    "id": "L1_T5_SCH_03",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Which is an example of sensitive personal information?",
    "question_en": "Which is an example of sensitive personal information?",
    "question_hi": "संवेदनशील व्यक्तिगत जानकारी (Sensitive Personal Data) का उदाहरण कौन सा है?",
    "options": [
      "A public weather report",
      "A person's password or bank details",
      "A general science fact",
      "A public school holiday date"
    ],
    "options_en": [
      "A public weather report",
      "A person's password or bank details",
      "A general science fact",
      "A public school holiday date"
    ],
    "options_hi": [
      "सार्वजनिक मौसम रिपोर्ट",
      "किसी व्यक्ति का पासवर्ड या बैंक विवरण",
      "सामान्य विज्ञान का तथ्य",
      "स्कूल की सार्वजनिक छुट्टी की तारीख"
    ],
    "answer": "A person's password or bank details",
    "correctAnswerIndex": 1,
    "explanation": "Passwords, financial details, and government IDs are private sensitive information requiring protection.",
    "explanation_en": "Passwords, financial details, and government IDs are private sensitive information requiring protection.",
    "explanation_hi": "पासवर्ड, बैंक खाता विवरण और आधार/पहचान पत्र अत्यंत संवेदनशील जानकारी हैं जिन्हें कभी उजागर नहीं करना चाहिए।"
  },
  {
    "id": "L1_T5_SCH_04",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Why should you check recipients before sending a file?",
    "question_en": "Why should you check recipients before sending a file?",
    "question_hi": "कोई फ़ाइल भेजने से पहले आपको प्राप्तकर्ताओं (Recipients) की जाँच क्यों करनी चाहिए?",
    "options": [
      "To reduce the chance of sharing information with the wrong person",
      "To make the file colourful",
      "To increase Wi-Fi range",
      "To remove the need for passwords"
    ],
    "options_en": [
      "To reduce the chance of sharing information with the wrong person",
      "To make the file colourful",
      "To increase Wi-Fi range",
      "To remove the need for passwords"
    ],
    "options_hi": [
      "गलत व्यक्ति के साथ जानकारी साझा होने की संभावना को कम करने के लिए",
      "फ़ाइल को रंगीन बनाने के लिए",
      "वाई-फ़ाई रेंज बढ़ाने के लिए",
      "पासवर्ड की आवश्यकता को समाप्त करने के लिए"
    ],
    "answer": "To reduce the chance of sharing information with the wrong person",
    "correctAnswerIndex": 0,
    "explanation": "Double-checking email addresses and group members prevents accidental data disclosure.",
    "explanation_en": "Double-checking email addresses and group members prevents accidental data disclosure.",
    "explanation_hi": "ईमेल या फ़ाइल भेजने से पहले प्राप्तकर्ता का नाम जांचने से गोपनीय फ़ाइल गलत हाथों में जाने से बचती है।"
  },
  {
    "id": "L1_T5_SCH_05",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "What does data minimization mean?",
    "question_en": "What does data minimization mean?",
    "question_hi": "डेटा मिनिमाइजेशन (Data Minimization) का क्या अर्थ है?",
    "options": [
      "Collecting or sharing only the data that is needed",
      "Saving every detail forever",
      "Sharing all files publicly",
      "Using the same password"
    ],
    "options_en": [
      "Collecting or sharing only the data that is needed",
      "Saving every detail forever",
      "Sharing all files publicly",
      "Using the same password"
    ],
    "options_hi": [
      "केवल वही डेटा एकत्र या साझा करना जो वास्तव में आवश्यक हो",
      "हर विवरण को हमेशा के लिए सहेजना",
      "सभी फ़ाइलों को सार्वजनिक रूप से साझा करना",
      "एक ही पासवर्ड का उपयोग करना"
    ],
    "answer": "Collecting or sharing only the data that is needed",
    "correctAnswerIndex": 0,
    "explanation": "Data minimization restricts data collection to what is strictly necessary for a specific objective.",
    "explanation_en": "Data minimization restricts data collection to what is strictly necessary for a specific objective.",
    "explanation_hi": "डेटा मिनिमाइजेशन का सिद्धांत कहता है कि काम के लिए केवल उतना ही डेटा इकट्ठा या शेयर किया जाए जितनी ज़रूरत हो।"
  },
  {
    "id": "L1_T5_SCH_06",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Which action helps protect a lost phone's information?",
    "question_en": "Which action helps protect a lost phone's information?",
    "question_hi": "खोए हुए फ़ोन में मौजूद जानकारी की सुरक्षा के लिए कौन सा उपाय मदद करता है?",
    "options": [
      "Leave it unlocked",
      "Use a screen lock and report the loss quickly",
      "Post its passcode online",
      "Disable every security feature"
    ],
    "options_en": [
      "Leave it unlocked",
      "Use a screen lock and report the loss quickly",
      "Post its passcode online",
      "Disable every security feature"
    ],
    "options_hi": [
      "इसे अनलॉक छोड़ दें",
      "स्क्रीन लॉक (पिन/बायोमेट्रिक) का उपयोग करें और तुरंत नुकसान की सूचना दें",
      "इसका पासकोड ऑनलाइन पोस्ट करें",
      "हर सुरक्षा सुविधा को अक्षम करें"
    ],
    "answer": "Use a screen lock and report the loss quickly",
    "correctAnswerIndex": 1,
    "explanation": "A strong screen passcode prevents strangers from accessing data, allowing time for remote wiping.",
    "explanation_en": "A strong screen passcode prevents strangers from accessing data, allowing time for remote wiping.",
    "explanation_hi": "स्क्रीन लॉक लगे होने से फोन खोने पर कोई डेटा नहीं देख सकता और आप उसे रिमोटली मिटा सकते हैं।"
  },
  {
    "id": "L1_T5_SCH_07",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Why are privacy settings useful on social media?",
    "question_en": "Why are privacy settings useful on social media?",
    "question_hi": "सोशल मीडिया पर प्राइवेसी सेटिंग्स (Privacy Settings) क्यों उपयोगी हैं?",
    "options": [
      "They help control who can view your posts and details",
      "They guarantee no scam can happen",
      "They make all posts anonymous",
      "They replace careful sharing"
    ],
    "options_en": [
      "They help control who can view your posts and details",
      "They guarantee no scam can happen",
      "They make all posts anonymous",
      "They replace careful sharing"
    ],
    "options_hi": [
      "वे यह नियंत्रित करने में मदद करती हैं कि आपकी पोस्ट और विवरण कौन देख सकता है",
      "वे गारंटी देती हैं कि कोई घोटाला नहीं हो सकता",
      "वे सभी पोस्ट को गुमनाम बनाती हैं",
      "वे सावधानीपूर्वक साझा करने की जगह लेती हैं"
    ],
    "answer": "They help control who can view your posts and details",
    "correctAnswerIndex": 0,
    "explanation": "Privacy settings prevent unknown strangers from accessing your photos, location, and personal updates.",
    "explanation_en": "Privacy settings prevent unknown strangers from accessing your photos, location, and personal updates.",
    "explanation_hi": "प्राइवेसी सेटिंग्स से आप चुन सकते हैं कि केवल आपके जाने-पहचाने दोस्त ही आपकी पोस्ट और प्रोफ़ाइल देख सकें।"
  },
  {
    "id": "L1_T5_SCH_08",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "What is a data breach?",
    "question_en": "What is a data breach?",
    "question_hi": "डेटा ब्रीच (Data Breach) क्या होता है?",
    "options": [
      "An incident where protected information is accessed, exposed, or stolen without permission",
      "A planned software update",
      "A routine computer restart",
      "A new wallpaper"
    ],
    "options_en": [
      "An incident where protected information is accessed, exposed, or stolen without permission",
      "A planned software update",
      "A routine computer restart",
      "A new wallpaper"
    ],
    "options_hi": [
      "एक ऐसी घटना जिसमें बिना अनुमति के सुरक्षित जानकारी देखी, उजागर या चुरा ली जाती है",
      "एक नियोजित सॉफ़्टवेयर अपडेट",
      "नियमित कंप्यूटर रीस्टार्ट",
      "एक नया वॉलपेपर"
    ],
    "answer": "An incident where protected information is accessed, exposed, or stolen without permission",
    "correctAnswerIndex": 0,
    "explanation": "A data breach involves security violations where sensitive or confidential records are exfiltrated.",
    "explanation_en": "A data breach involves security violations where sensitive or confidential records are exfiltrated.",
    "explanation_hi": "डेटा ब्रीच वह सुरक्षा विफलता है जिसमें सुरक्षा घेरा तोड़कर हैकर गोपनीय डेटा चुरा लेते हैं।"
  },
  {
    "id": "L1_T5_SCH_09",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Which is a safer way to share a confidential document?",
    "question_en": "Which is a safer way to share a confidential document?",
    "question_hi": "एक गोपनीय दस्तावेज़ साझा करने का अधिक सुरक्षित तरीका कौन सा है?",
    "options": [
      "Post it on a public page",
      "Use an approved service and restrict access to the intended people",
      "Send it to a random address",
      "Remove its filename only"
    ],
    "options_en": [
      "Post it on a public page",
      "Use an approved service and restrict access to the intended people",
      "Send it to a random address",
      "Remove its filename only"
    ],
    "options_hi": [
      "इसे किसी सार्वजनिक पेज पर पोस्ट करें",
      "स्वीकृत क्लाउड सेवा का उपयोग करें और केवल अधिकृत लोगों तक पहुँच सीमित करें",
      "इसे किसी भी यादृच्छिक पते पर भेजें",
      "केवल उसका फ़ाइल नाम हटा दें"
    ],
    "answer": "Use an approved service and restrict access to the intended people",
    "correctAnswerIndex": 1,
    "explanation": "Use authenticated cloud storage with specific read/write permissions rather than public links.",
    "explanation_en": "Use authenticated cloud storage with specific read/write permissions rather than public links.",
    "explanation_hi": "गोपनीय फ़ाइल साझा करते समय केवल संबंधित व्यक्ति के ईमेल पते पर ही सीमित अनुमति देनी चाहिए।"
  },
  {
    "id": "L1_T5_SCH_10",
    "level": 1,
    "topic": "Data Leak",
    "topicId": "data_leak",
    "mode": "school",
    "question": "Why should organizations limit who can access personal data?",
    "question_en": "Why should organizations limit who can access personal data?",
    "question_hi": "संगठनों को व्यक्तिगत डेटा तक पहुँच को सीमित क्यों करना चाहिए?",
    "options": [
      "To reduce accidental exposure and misuse",
      "To make all data public",
      "To stop all software updates",
      "To remove the need for staff training"
    ],
    "options_en": [
      "To reduce accidental exposure and misuse",
      "To make all data public",
      "To stop all software updates",
      "To remove the need for staff training"
    ],
    "options_hi": [
      "आकस्मिक खुलासे और दुरुपयोग के जोखिम को कम करने के लिए",
      "सभी डेटा को सार्वजनिक करने के लिए",
      "सभी सॉफ़्टवेयर अपडेट बंद करने के लिए",
      "कर्मचारी प्रशिक्षण की आवश्यकता को समाप्त करने के लिए"
    ],
    "answer": "To reduce accidental exposure and misuse",
    "correctAnswerIndex": 0,
    "explanation": "Restricting access based on need-to-know minimizes internal threats and unintended leaks.",
    "explanation_en": "Restricting access based on need-to-know minimizes internal threats and unintended leaks.",
    "explanation_hi": "डेटा तक पहुँच सीमित रखने से डेटा लीक होने और उसके दुरुपयोग की संभावना बहुत कम हो जाती है।"
  }
]

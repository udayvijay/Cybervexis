# -*- coding: utf-8 -*-
"""Level 5: Cyber Resilience (5 topics x 10 questions = 50 questions)"""

level5_questions = [
  # Topic 21 (L5 T1): Preventive Resilience
  {
    "id": "L5_T1_SCH_01",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Which action is an example of preventive cybersecurity?",
    "question_en": "Which action is an example of preventive cybersecurity?",
    "question_hi": "निवारक साइबर सुरक्षा (Preventive Cybersecurity) का एक उदाहरण कौन सा है?",
    "options": [
      "Installing security updates before a known weakness is exploited",
      "Ignoring warnings",
      "Sharing passwords",
      "Deleting all backups"
    ],
    "options_en": [
      "Installing security updates before a known weakness is exploited",
      "Ignoring warnings",
      "Sharing passwords",
      "Deleting all backups"
    ],
    "options_hi": [
      "किसी ज्ञात कमज़ोरी का शोषण होने से पहले ही सुरक्षा अपडेट इंस्टॉल करना",
      "चेतावनियों को अनदेखा करना",
      "पासवर्ड साझा करना",
      "सभी बैकअप हटाना"
    ],
    "answer": "Installing security updates before a known weakness is exploited",
    "correctAnswerIndex": 0,
    "explanation": "Preventive controls defend systems proactively before attackers have the opportunity to exploit vulnerabilities.",
    "explanation_en": "Installing security updates before a known weakness is exploited.",
    "explanation_hi": "निवारक सुरक्षा का अर्थ है हमला होने से पहले ही कमज़ोरियों को ठीक करके खुद को तैयार रखना।"
  },
  {
    "id": "L5_T1_SCH_02",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Why is least privilege a preventive measure?",
    "question_en": "Why is least privilege a preventive measure?",
    "question_hi": "न्यूनतम विशेषाधिकार (Least Privilege) एक निवारक उपाय क्यों है?",
    "options": [
      "It limits what an account can do if it is misused",
      "It gives everyone full access",
      "It makes phishing messages disappear",
      "It removes the need for passwords"
    ],
    "options_en": [
      "It limits what an account can do if it is misused",
      "It gives everyone full access",
      "It makes phishing messages disappear",
      "It removes the need for passwords"
    ],
    "options_hi": [
      "यह खाता हैक या दुरुपयोग होने की स्थिति में संभावित नुकसान को सीमित करता है",
      "यह सभी को पूर्ण एक्सेस देता है",
      "यह फ़िशिंग संदेशों को गायब कर देता है",
      "यह पासवर्ड की आवश्यकता को समाप्त करता है"
    ],
    "answer": "It limits what an account can do if it is misused",
    "correctAnswerIndex": 0,
    "explanation": "Restricting user permissions prevents a compromised standard account from performing unauthorized system changes.",
    "explanation_en": "It limits what an account can do if it is misused.",
    "explanation_hi": "यदि किसी सामान्य खाते को सीमित अधिकार मिले हों, तो हैकर उसके ज़रिए पूरे नेटवर्क को नुकसान नहीं पहुँचा सकता।"
  },
  {
    "id": "L5_T1_SCH_03",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Which is the best way to reduce phishing risk?",
    "question_en": "Which is the best way to reduce phishing risk?",
    "question_hi": "फ़िशिंग के जोखिम को कम करने का सबसे अच्छा तरीका कौन सा है?",
    "options": [
      "Learn warning signs and verify unexpected requests",
      "Click every urgent link",
      "Reply with account details",
      "Trust every display name"
    ],
    "options_en": [
      "Learn warning signs and verify unexpected requests",
      "Click every urgent link",
      "Reply with account details",
      "Trust every display name"
    ],
    "options_hi": [
      "चेतावनी के संकेतों को पहचानना सीखना और अप्रत्याशित ईमेल/अनुरोधों की स्वतंत्र रूप से पुष्टि करना",
      "हर जरूरी दिखने वाले लिंक पर क्लिक करना",
      "खाता विवरण के साथ उत्तर देना",
      "ईमेल में दिखने वाले हर नाम पर आँख मूंदकर भरोसा करना"
    ],
    "answer": "Learn warning signs and verify unexpected requests",
    "correctAnswerIndex": 0,
    "explanation": "Security training empowers users to recognize red flags like suspicious domains and false urgency.",
    "explanation_en": "Learn warning signs and verify unexpected requests.",
    "explanation_hi": "संदिग्ध लिंक और झूठी जल्दबाजी जैसे फ़िशिंग संकेतों को पहचानना ही सबसे सुरक्षित बचाव है।"
  },
  {
    "id": "L5_T1_SCH_04",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Why are regular backups part of preparation?",
    "question_en": "Why are regular backups part of preparation?",
    "question_hi": "नियमित बैकअप साइबर सुरक्षा तैयारी का हिस्सा क्यों हैं?",
    "options": [
      "They can help recover data after loss or an attack",
      "They stop every suspicious email",
      "They replace all security controls",
      "They make data public"
    ],
    "options_en": [
      "They can help recover data after loss or an attack",
      "They stop every suspicious email",
      "They replace all security controls",
      "They make data public"
    ],
    "options_hi": [
      "वे डेटा हानि या रैनसमवेयर हमले के बाद जानकारी को सुरक्षित रूप से पुनर्प्राप्त करने में मदद करते हैं",
      "वे हर संदिग्ध ईमेल को रोकते हैं",
      "वे सभी सुरक्षा नियंत्रणों की जगह लेते हैं",
      "वे डेटा को सार्वजनिक बनाते हैं"
    ],
    "answer": "They can help recover data after loss or an attack",
    "correctAnswerIndex": 0,
    "explanation": "Regular backups guarantee operational continuity if ransomware or disk failure strikes.",
    "explanation_en": "They can help recover data after loss or an attack.",
    "explanation_hi": "यदि कंप्यूटर पर कोई हमला हो जाए या फ़ाइलें डिलीट हो जाएं, तो बैकअप से डेटा वापस पाया जा सकता है।"
  },
  {
    "id": "L5_T1_SCH_05",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "What is the purpose of a cybersecurity policy?",
    "question_en": "What is the purpose of a cybersecurity policy?",
    "question_hi": "साइबर सुरक्षा नीति (Cybersecurity Policy) का क्या उद्देश्य है?",
    "options": [
      "To explain safe and approved ways to use systems and data",
      "To list everyone's passwords",
      "To remove all restrictions",
      "To guarantee no incidents"
    ],
    "options_en": [
      "To explain safe and approved ways to use systems and data",
      "To list everyone's passwords",
      "To remove all restrictions",
      "To guarantee no incidents"
    ],
    "options_hi": [
      "सिस्टम और डेटा के उपयोग के सुरक्षित और स्वीकृत तरीकों को स्पष्ट रूप से समझाना",
      "सभी के पासवर्ड सूचीबद्ध करना",
      "सभी प्रतिबंधों को हटाना",
      "किसी घटना न होने की गारंटी देना"
    ],
    "answer": "To explain safe and approved ways to use systems and data",
    "correctAnswerIndex": 0,
    "explanation": "Policies outline acceptable use, password standards, and safe operational guidelines for all stakeholders.",
    "explanation_en": "To explain safe and approved ways to use systems and data.",
    "explanation_hi": "सुरक्षा नीति सभी छात्रों और शिक्षकों को बताती है कि कंप्यूटर और इंटरनेट का सुरक्षित उपयोग कैसे करना है।"
  },
  {
    "id": "L5_T1_SCH_06",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Which practice reduces the risk of installing malware?",
    "question_en": "Which practice reduces the risk of installing malware?",
    "question_hi": "इनमें से कौन सा अभ्यास मैलवेयर इंस्टॉल होने के जोखिम को कम करता है?",
    "options": [
      "Download software from trusted sources and check permissions",
      "Use unknown cracked software",
      "Disable security warnings",
      "Open every email attachment"
    ],
    "options_en": [
      "Download software from trusted sources and check permissions",
      "Use unknown cracked software",
      "Disable security warnings",
      "Open every email attachment"
    ],
    "options_hi": [
      "केवल विश्वसनीय आधिकारिक स्रोतों से सॉफ़्टवेयर डाउनलोड करना और ऐप अनुमतियों की जांच करना",
      "अज्ञात क्रैक किए गए सॉफ़्टवेयर का उपयोग करना",
      "सुरक्षा चेतावनियों को अक्षम करना",
      "हर ईमेल अटैचमेंट को खोलना"
    ],
    "answer": "Download software from trusted sources and check permissions",
    "correctAnswerIndex": 0,
    "explanation": "Downloading software solely from verified repositories protects devices from trojans.",
    "explanation_en": "Download software from trusted sources and check permissions.",
    "explanation_hi": "हमेशा अधिकृत ऐप स्टोर से ही डाउनलोड करना और गैर-ज़रूरी परमिशन न देना मैलवेयर से बचाता है।"
  },
  {
    "id": "L5_T1_SCH_07",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Why conduct security awareness training?",
    "question_en": "Why conduct security awareness training?",
    "question_hi": "सुरक्षा जागरूकता प्रशिक्षण (Security Awareness Training) क्यों आयोजित किया जाता है?",
    "options": [
      "To help people recognize threats and respond safely",
      "To make attacks impossible",
      "To remove the need for updates",
      "To share passwords more easily"
    ],
    "options_en": [
      "To help people recognize threats and respond safely",
      "To make attacks impossible",
      "To remove the need for updates",
      "To share passwords more easily"
    ],
    "options_hi": [
      "लोगों को साइबर खतरों को पहचानने और सुरक्षित तरीके से प्रतिक्रिया देने में सक्षम बनाने के लिए",
      "हमलों को पूरी तरह असंभव बनाने के लिए",
      "अपडेट की आवश्यकता को समाप्त करने के लिए",
      "पासवर्ड अधिक आसानी से साझा करने के लिए"
    ],
    "answer": "To help people recognize threats and respond safely",
    "correctAnswerIndex": 0,
    "explanation": "Awareness training builds a human firewall, turning employees and students into an active defensive asset.",
    "explanation_en": "To help people recognize threats and respond safely.",
    "explanation_hi": "जागरूकता प्रशिक्षण से छात्र और शिक्षक समझ पाते हैं कि संदिग्ध लिंक, वायरस और फ़िशिंग से कैसे बचना है।"
  },
  {
    "id": "L5_T1_SCH_08",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "What does vulnerability management involve?",
    "question_en": "What does vulnerability management involve?",
    "question_hi": "कमज़ोरी प्रबंधन (Vulnerability Management) में क्या शामिल है?",
    "options": [
      "Finding, prioritizing, and fixing security weaknesses",
      "Making all files public",
      "Changing desktop wallpaper",
      "Ignoring outdated systems"
    ],
    "options_en": [
      "Finding, prioritizing, and fixing security weaknesses",
      "Making all files public",
      "Changing desktop wallpaper",
      "Ignoring outdated systems"
    ],
    "options_hi": [
      "सिस्टम की सुरक्षा कमज़ोरियों को खोजना, उनकी प्राथमिकता तय करना और उन्हें ठीक (पैच) करना",
      "सभी फ़ाइलों को सार्वजनिक करना",
      "डेस्कटॉप वॉलपेपर बदलना",
      "पुराने सिस्टम को अनदेखा करना"
    ],
    "answer": "Finding, prioritizing, and fixing security weaknesses",
    "correctAnswerIndex": 0,
    "explanation": "Continuous vulnerability assessment identifies flaws before threat actors discover and exploit them.",
    "explanation_en": "Finding, prioritizing, and fixing security weaknesses.",
    "explanation_hi": "सिस्टम में मौजूद कमज़ोरियों को समय रहते ढूंढकर पैच करना कमज़ोरी प्रबंधन कहलाता है।"
  },
  {
    "id": "L5_T1_SCH_09",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Why should organizations test their security controls?",
    "question_en": "Why should organizations test their security controls?",
    "question_hi": "संगठनों को अपने सुरक्षा नियंत्रणों का परीक्षण क्यों करना चाहिए?",
    "options": [
      "To check whether protections work as expected",
      "To guarantee zero risk forever",
      "To delete all logs",
      "To stop staff asking questions"
    ],
    "options_en": [
      "To check whether protections work as expected",
      "To guarantee zero risk forever",
      "To delete all logs",
      "To stop staff asking questions"
    ],
    "options_hi": [
      "यह सत्यापित करने के लिए कि सभी सुरक्षा उपाय और फ़ायरवॉल अपेक्षानुसार काम कर रहे हैं",
      "हमेशा के लिए शून्य जोखिम की गारंटी देने के लिए",
      "सभी लॉग्स को हटाने के लिए",
      "कर्मचारियों को सवाल पूछने से रोकने के लिए"
    ],
    "answer": "To check whether protections work as expected",
    "correctAnswerIndex": 0,
    "explanation": "Audits, penetration tests, and tabletop simulations validate that defensive configurations function under attack.",
    "explanation_en": "To check whether protections work as expected.",
    "explanation_hi": "सुरक्षा उपायों का समय-समय पर परीक्षण करने से यह सुनिश्चित होता है कि हमला होने पर वे वास्तव में रक्षा करेंगे।"
  },
  {
    "id": "L5_T1_SCH_10",
    "level": 5,
    "topic": "Preventive Resilience",
    "topicId": "preventive_resilience",
    "mode": "school",
    "question": "Which is the strongest preventive approach?",
    "question_en": "Which is the strongest preventive approach?",
    "question_hi": "इनमें से कौन सा सबसे मजबूत निवारक दृष्टिकोण है?",
    "options": [
      "Use several appropriate safeguards together",
      "Rely only on one password",
      "Trust every download",
      "Disable all updates"
    ],
    "options_en": [
      "Use several appropriate safeguards together",
      "Rely only on one password",
      "Trust every download",
      "Disable all updates"
    ],
    "options_hi": [
      "एक साथ कई उपयुक्त सुरक्षा उपायों (Defense in Depth) का उपयोग करना",
      "केवल एक पासवर्ड पर निर्भर रहना",
      "हर डाउनलोड पर भरोसा करना",
      "सभी अपडेट अक्षम करना"
    ],
    "answer": "Use several appropriate safeguards together",
    "correctAnswerIndex": 0,
    "explanation": "Layered defense (Defense in Depth) ensures that if one barrier fails, subsequent controls prevent a full breach.",
    "explanation_en": "Use several appropriate safeguards together.",
    "explanation_hi": "मजबूत पासवर्ड, फ़ायरवॉल, एंटीवायरस और MFA जैसे कई सुरक्षा स्तर एक साथ लगाने से सबसे मजबूत सुरक्षा मिलती है।"
  },

  # Topic 22 (L5 T2): Detective Resilience
  {
    "id": "L5_T2_SCH_01",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "Which could be a sign of a compromised account?",
    "question_en": "Which could be a sign of a compromised account?",
    "question_hi": "किसी खाते के हैक (समझौता) होने का एक लक्षण कौन सा हो सकता है?",
    "options": [
      "A login from an unfamiliar place that the user cannot explain",
      "A normal login at the usual time",
      "A saved offline file",
      "A planned software update"
    ],
    "options_en": [
      "A login from an unfamiliar place that the user cannot explain",
      "A normal login at the usual time",
      "A saved offline file",
      "A planned software update"
    ],
    "options_hi": [
      "किसी अनजान स्थान या देश से ऐसा लॉगिन जिसकी उपयोगकर्ता पुष्टि न कर सके",
      "सामान्य समय पर एक सामान्य लॉगिन",
      "एक सहेजी गई ऑफ़लाइन फ़ाइल",
      "एक नियोजित सॉफ़्टवेयर अपडेट"
    ],
    "answer": "A login from an unfamiliar place that the user cannot explain",
    "correctAnswerIndex": 0,
    "explanation": "Unexpected geographical logins or impossible travel alerts indicate stolen session tokens or credentials.",
    "explanation_en": "A login from an unfamiliar place that the user cannot explain.",
    "explanation_hi": "यदि आपके खाते में किसी अनजान शहर या असामान्य समय पर लॉगिन दिखाई दे, तो इसका मतलब है कि कोई दूसरा आपका पासवर्ड जानता है।"
  },
  {
    "id": "L5_T2_SCH_02",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "What are system logs useful for?",
    "question_en": "What are system logs useful for?",
    "question_hi": "सिस्टम लॉग्स (System Logs) किसलिए उपयोगी होते हैं?",
    "options": [
      "Recording events that can help detect and investigate activity",
      "Storing passwords for public use",
      "Making a screen brighter",
      "Replacing every backup"
    ],
    "options_en": [
      "Recording events that can help detect and investigate activity",
      "Storing passwords for public use",
      "Making a screen brighter",
      "Replacing every backup"
    ],
    "options_hi": [
      "ऐसी घटनाओं को रिकॉर्ड करने के लिए जो गतिविधियों का पता लगाने और जांच करने में मदद कर सकें",
      "सार्वजनिक उपयोग के लिए पासवर्ड संग्रहीत करना",
      "स्क्रीन को अधिक चमकदार बनाना",
      "प्रत्येक बैकअप की जगह लेना"
    ],
    "answer": "Recording events that can help detect and investigate activity",
    "correctAnswerIndex": 0,
    "explanation": "Audit logs record authentication attempts, network flows, and file accesses for security monitoring.",
    "explanation_en": "Recording events that can help detect and investigate activity.",
    "explanation_hi": "सिस्टम लॉग्स कंप्यूटर पर होने वाले हर कार्य का समय और विवरण दर्ज करते हैं जिससे गड़बड़ी पकड़ी जा सकती है।"
  },
  {
    "id": "L5_T2_SCH_03",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "What is a security alert?",
    "question_en": "What is a security alert?",
    "question_hi": "सुरक्षा अलर्ट (Security Alert) क्या होता है?",
    "options": [
      "A notification about activity that may need investigation",
      "A guarantee that an attack happened",
      "A kind of charger",
      "A new keyboard"
    ],
    "options_en": [
      "A notification about activity that may need investigation",
      "A guarantee that an attack happened",
      "A kind of charger",
      "A new keyboard"
    ],
    "options_hi": [
      "किसी ऐसी असामान्य या संदिग्ध गतिविधि के बारे में सूचना जिसकी जांच की आवश्यकता हो सकती है",
      "यह गारंटी कि हमला हुआ ही है",
      "एक प्रकार का चार्जर",
      "एक नया कीबोर्ड"
    ],
    "answer": "A notification about activity that may need investigation",
    "correctAnswerIndex": 0,
    "explanation": "Security monitoring tools trigger alerts whenever behavioral baselines or security rules are tripped.",
    "explanation_en": "A notification about activity that may need investigation.",
    "explanation_hi": "सुरक्षा अलर्ट एक चेतावनी होती है जो बताती है कि सिस्टम पर कुछ असामान्य हुआ है जिसकी तुरंत जांच होनी चाहिए।"
  },
  {
    "id": "L5_T2_SCH_04",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "What should an analyst do with an alert?",
    "question_en": "What should an analyst do with an alert?",
    "question_hi": "एक सुरक्षा विश्लेषक को प्राप्त अलर्ट के साथ क्या करना चाहिए?",
    "options": [
      "Review the evidence and follow the response process",
      "Assume every alert is false",
      "Delete it without checking",
      "Post it publicly with user details"
    ],
    "options_en": [
      "Review the evidence and follow the response process",
      "Assume every alert is false",
      "Delete it without checking",
      "Post it publicly with user details"
    ],
    "options_hi": [
      "साक्ष्यों की समीक्षा करें और स्थापित घटना-प्रतिक्रिया प्रक्रिया का पालन करें",
      "मान लें कि हर अलर्ट झूठा है",
      "बिना जांचे इसे हटा दें",
      "उपयोगकर्ता विवरण के साथ इसे सार्वजनिक रूप से पोस्ट करें"
    ],
    "answer": "Review the evidence and follow the response process",
    "correctAnswerIndex": 0,
    "explanation": "Analysts investigate indicators, assess context, and either dismiss false positives or escalate real threats.",
    "explanation_en": "Review the evidence and follow the response process.",
    "explanation_hi": "विश्लेषक को अलर्ट के तकनीकी सबूतों की जांच करके नियमों के तहत आगे कदम उठाना चाहिए।"
  },
  {
    "id": "L5_T2_SCH_05",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "What is a false positive?",
    "question_en": "What is a false positive?",
    "question_hi": "फ़ाल्स पॉज़िटिव (False Positive) क्या है?",
    "options": [
      "A warning that turns out not to be a real security threat",
      "A confirmed attack",
      "A safe backup",
      "A strong password"
    ],
    "options_en": [
      "A warning that turns out not to be a real security threat",
      "A confirmed attack",
      "A safe backup",
      "A strong password"
    ],
    "options_hi": [
      "एक ऐसी चेतावनी जो जांच के बाद वास्तविक सुरक्षा खतरा नहीं निकलती (झूठा अलार्म)",
      "एक पुष्ट हमला",
      "एक सुरक्षित बैकअप",
      "एक मजबूत पासवर्ड"
    ],
    "answer": "A warning that turns out not to be a real security threat",
    "correctAnswerIndex": 0,
    "explanation": "False positives arise when benign activities resemble attack signatures and trigger defensive alarms.",
    "explanation_en": "A warning that turns out not to be a real security threat.",
    "explanation_hi": "जब कोई सामान्य गतिविधि गलती से सुरक्षा प्रणाली द्वारा खतरे के रूप में पहचान ली जाए, तो उसे फ़ाल्स पॉज़िटिव कहते हैं।"
  },
  {
    "id": "L5_T2_SCH_06",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "Why is early threat detection valuable?",
    "question_en": "Why is early threat detection valuable?",
    "question_hi": "खतरों का समय रहते शीघ्र पता लगाना (Early Detection) क्यों मूल्यवान है?",
    "options": [
      "It may allow a team to limit damage sooner",
      "It removes the need for response",
      "It makes every file public",
      "It guarantees no further threats"
    ],
    "options_en": [
      "It may allow a team to limit damage sooner",
      "It removes the need for response",
      "It makes every file public",
      "It guarantees no further threats"
    ],
    "options_hi": [
      "यह सुरक्षा टीम को नुकसान को जल्दी रोकने और हमला फैलने से पहले नियंत्रित करने की अनुमति देता है",
      "यह प्रतिक्रिया की आवश्यकता को समाप्त करता है",
      "यह हर फ़ाइल को सार्वजनिक बनाता है",
      "यह आगे कोई खतरा न होने की गारंटी देता है"
    ],
    "answer": "It may allow a team to limit damage sooner",
    "correctAnswerIndex": 0,
    "explanation": "Minimizing dwell time prevents adversaries from stealing credentials, deploying ransomware, or exfiltrating data.",
    "explanation_en": "It may allow a team to limit damage sooner.",
    "explanation_hi": "हमले का जल्दी पता चलने से हैकर को डेटा चुराने या पूरे नेटवर्क को लॉक करने से पहले ही रोका जा सकता है।"
  },
  {
    "id": "L5_T2_SCH_07",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "Which tool can help identify suspicious network activity?",
    "question_en": "Which tool can help identify suspicious network activity?",
    "question_hi": "संदिग्ध नेटवर्क गतिविधि की पहचान करने में कौन सा उपकरण मदद कर सकता है?",
    "options": [
      "A network monitoring or security detection tool",
      "A wallpaper editor",
      "A music player only",
      "A calculator"
    ],
    "options_en": [
      "A network monitoring or security detection tool",
      "A wallpaper editor",
      "A music player only",
      "A calculator"
    ],
    "options_hi": [
      "एक नेटवर्क निगरानी या सुरक्षा पहचान उपकरण (Network Monitoring / NIDS Tool)",
      "वॉलपेपर संपादक",
      "केवल एक संगीत प्लेयर",
      "एक कैलकुलेटर"
    ],
    "answer": "A network monitoring or security detection tool",
    "correctAnswerIndex": 0,
    "explanation": "Network Intrusion Detection Systems (NIDS) and SIEM tools analyze packet flows for anomalous behavior.",
    "explanation_en": "A network monitoring or security detection tool.",
    "explanation_hi": "नेटवर्क मॉनिटरिंग टूल्स सभी डेटा कनेक्शनों का विश्लेषण करके संदिग्ध हरकतों को तुरंत पकड़ते हैं।"
  },
  {
    "id": "L5_T2_SCH_08",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "Why should unusual account activity be investigated?",
    "question_en": "Why should unusual account activity be investigated?",
    "question_hi": "असामान्य खाता गतिविधि की जांच क्यों की जानी चाहिए?",
    "options": [
      "It could indicate misuse or unauthorized access",
      "It always means the user is guilty",
      "It automatically deletes data",
      "It makes the network faster"
    ],
    "options_en": [
      "It could indicate misuse or unauthorized access",
      "It always means the user is guilty",
      "It automatically deletes data",
      "It makes the network faster"
    ],
    "options_hi": [
      "यह अनधिकृत पहुँच या खाते के दुरुपयोग का संकेत हो सकता है",
      "इसका हमेशा मतलब होता है कि उपयोगकर्ता दोषी है",
      "यह स्वचालित रूप से डेटा हटा देता है",
      "यह नेटवर्क को तेज़ बनाता है"
    ],
    "answer": "It could indicate misuse or unauthorized access",
    "correctAnswerIndex": 0,
    "explanation": "Unusual file downloads or strange access hours often indicate hijacked accounts or insider threats.",
    "explanation_en": "It could indicate misuse or unauthorized access.",
    "explanation_hi": "असामान्य गतिविधियों की जांच करने से यह पता चलता है कि कहीं खाता किसी हैकर के कब्जे में तो नहीं चला गया।"
  },
  {
    "id": "L5_T2_SCH_09",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "What should a student do after noticing a suspicious message or login alert?",
    "question_en": "What should a student do after noticing a suspicious message or login alert?",
    "question_hi": "संदिग्ध संदेश या अनपेक्षित लॉगिन अलर्ट देखने के बाद छात्र को क्या करना चाहिए?",
    "options": [
      "Report it to a trusted adult or IT support",
      "Share passwords to confirm it",
      "Ignore it forever",
      "Forward it publicly"
    ],
    "options_en": [
      "Report it to a trusted adult or IT support",
      "Share passwords to confirm it",
      "Ignore it forever",
      "Forward it publicly"
    ],
    "options_hi": [
      "किसी विश्वसनीय वयस्क, शिक्षक या IT सहायता को तुरंत रिपोर्ट करें",
      "इसकी पुष्टि के लिए पासवर्ड साझा करें",
      "इसे हमेशा के लिए अनदेखा करें",
      "इसे सार्वजनिक रूप से फॉरवर्ड करें"
    ],
    "answer": "Report it to a trusted adult or IT support",
    "correctAnswerIndex": 0,
    "explanation": "Reporting suspicious alerts enables swift security triage and protects peers from broader campaigns.",
    "explanation_en": "Report it to a trusted adult or IT support.",
    "explanation_hi": "किसी भी संदिग्ध अलर्ट की तुरंत शिक्षक या IT टीम को सूचना देनी चाहिए ताकि समय रहते खाता सुरक्षित किया जा सके।"
  },
  {
    "id": "L5_T2_SCH_10",
    "level": 5,
    "topic": "Detective Resilience",
    "topicId": "detective_resilience",
    "mode": "school",
    "question": "Does detecting a threat automatically remove it?",
    "question_en": "Does detecting a threat automatically remove it?",
    "question_hi": "क्या किसी खतरे का पता लगाने से वह स्वचालित रूप से समाप्त हो जाता है?",
    "options": [
      "Yes, in every case",
      "No, a suitable response may still be needed",
      "Only when the computer is off",
      "Only if the alert is red"
    ],
    "options_en": [
      "Yes, in every case",
      "No, a suitable response may still be needed",
      "Only when the computer is off",
      "Only if the alert is red"
    ],
    "options_hi": [
      "हाँ, हर मामले में",
      "नहीं, खतरे को रोकने और साफ़ करने के लिए एक उचित प्रतिक्रिया (Response) की आवश्यकता होती है",
      "केवल जब कंप्यूटर बंद हो",
      "केवल तभी जब अलर्ट लाल रंग का हो"
    ],
    "answer": "No, a suitable response may still be needed",
    "correctAnswerIndex": 1,
    "explanation": "Detection alerts responders to danger, but containment and eradication actions are required to neutralize it.",
    "explanation_en": "No, a suitable response may still be needed.",
    "explanation_hi": "खतरे का पता चलना केवल पहला कदम है; इसके बाद वायरस को हटाना और सिस्टम ठीक करना भी ज़रूरी होता है।"
  },

  # Topic 23 (L5 T3): Responsive Resilience
  {
    "id": "L5_T3_SCH_01",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "What is the main aim of incident response?",
    "question_en": "What is the main aim of incident response?",
    "question_hi": "घटना प्रतिक्रिया (Incident Response) का मुख्य उद्देश्य क्या है?",
    "options": [
      "Control the incident, reduce harm, and restore safe operation",
      "Hide all evidence",
      "Share passwords publicly",
      "Ignore affected systems"
    ],
    "options_en": [
      "Control the incident, reduce harm, and restore safe operation",
      "Hide all evidence",
      "Share passwords publicly",
      "Ignore affected systems"
    ],
    "options_hi": [
      "घटना को नियंत्रित करना, नुकसान को कम करना और सुरक्षित संचालन को बहाल करना",
      "सभी सबूत छिपाना",
      "पासवर्ड सार्वजनिक रूप से साझा करना",
      "प्रभावित प्रणालियों को अनदेखा करना"
    ],
    "answer": "Control the incident, reduce harm, and restore safe operation",
    "correctAnswerIndex": 0,
    "explanation": "Incident response focuses on containment, eradication of attackers, and rapid business recovery.",
    "explanation_en": "Control the incident, reduce harm, and restore safe operation.",
    "explanation_hi": "घटना प्रतिक्रिया का उद्देश्य हमले को फैलने से रोकना, नुकसान सीमित करना और प्रणालियों को पुनः चालू करना है।"
  },
  {
    "id": "L5_T3_SCH_02",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "What does containment mean during a cyber incident?",
    "question_en": "What does containment mean during a cyber incident?",
    "question_hi": "साइबर घटना के दौरान रोकथाम / नियंत्रण (Containment) का क्या अर्थ है?",
    "options": [
      "Limiting the spread or impact of the incident",
      "Deleting every backup",
      "Giving all users administrator access",
      "Publishing system logs"
    ],
    "options_en": [
      "Limiting the spread or impact of the incident",
      "Deleting every backup",
      "Giving all users administrator access",
      "Publishing system logs"
    ],
    "options_hi": [
      "घटना के प्रसार या प्रभाव को सीमित करना (हमले को अन्य कंप्यूटरों में फैलने से रोकना)",
      "हर बैकअप को हटाना",
      "सभी उपयोगकर्ताओं को व्यवस्थापक एक्सेस देना",
      "सिस्टम लॉग प्रकाशित करना"
    ],
    "answer": "Limiting the spread or impact of the incident",
    "correctAnswerIndex": 0,
    "explanation": "Containment isolates compromised segments or machines to stop malware from propagating further.",
    "explanation_en": "Limiting the spread or impact of the incident.",
    "explanation_hi": "कंटेनमेंट का अर्थ है संक्रमित कंप्यूटर को नेटवर्क से अलग करना ताकि वायरस बाकी कंप्यूटरों में न पहुंचे।"
  },
  {
    "id": "L5_T3_SCH_03",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "A school computer may be infected. What is a sensible action?",
    "question_en": "A school computer may be infected. What is a sensible action?",
    "question_hi": "एक स्कूल कंप्यूटर के संक्रमित होने का संदेह है। क्या एक समझदारी भरा कदम है?",
    "options": [
      "Follow school procedures and contact IT support promptly",
      "Keep opening suspicious files",
      "Enter passwords into pop-ups",
      "Disable every security tool"
    ],
    "options_en": [
      "Follow school procedures and contact IT support promptly",
      "Keep opening suspicious files",
      "Enter passwords into pop-ups",
      "Disable every security tool"
    ],
    "options_hi": [
      "स्कूल की प्रक्रियाओं का पालन करें और तुरंत IT सहायता/शिक्षक से संपर्क करें",
      "संदिग्ध फ़ाइलें खोलना जारी रखें",
      "पॉप-अप में पासवर्ड दर्ज करें",
      "हर सुरक्षा उपकरण को अक्षम करें"
    ],
    "answer": "Follow school procedures and contact IT support promptly",
    "correctAnswerIndex": 0,
    "explanation": "Early notification allows technical staff to disconnect the machine and start malware disinfection.",
    "explanation_en": "Follow school procedures and contact IT support promptly.",
    "explanation_hi": "संक्रमित कंप्यूटर की तुरंत IT शिक्षक को सूचना देनी चाहिए ताकि वे उसे अलग करके ठीक कर सकें।"
  },
  {
    "id": "L5_T3_SCH_04",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "Why should incident details be documented?",
    "question_en": "Why should incident details be documented?",
    "question_hi": "घटना के विवरण का दस्तावेज़ीकरण (Documentation) क्यों किया जाना चाहिए?",
    "options": [
      "They help investigation, coordination, and later improvement",
      "They make the incident disappear",
      "They replace all security tools",
      "They make passwords public"
    ],
    "options_en": [
      "They help investigation, coordination, and later improvement",
      "They make the incident disappear",
      "They replace all security tools",
      "They make passwords public"
    ],
    "options_hi": [
      "वे जांच, टीम समन्वय और बाद में सुरक्षा सुधार में मदद करते हैं",
      "वे घटना को गायब कर देते हैं",
      "वे सभी सुरक्षा उपकरणों की जगह लेते हैं",
      "वे पासवर्ड सार्वजनिक करते हैं"
    ],
    "answer": "They help investigation, coordination, and later improvement",
    "correctAnswerIndex": 0,
    "explanation": "Accurate timelines and artifact tracking provide legal evidence and drive root-cause improvements.",
    "explanation_en": "They help investigation, coordination, and later improvement.",
    "explanation_hi": "रिकॉर्ड रखने से जांच में आसानी होती है और भविष्य में उसी तरह की गलती दोहराने से बचा जा सकता है।"
  },
  {
    "id": "L5_T3_SCH_05",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "Why should evidence be preserved during an investigation?",
    "question_en": "Why should evidence be preserved during an investigation?",
    "question_hi": "जांच के दौरान साक्ष्य (Evidence) को संरक्षित क्यों किया जाना चाहिए?",
    "options": [
      "It may help determine what happened and how to respond",
      "It makes all malware harmless",
      "It prevents every future attack",
      "It replaces backups"
    ],
    "options_en": [
      "It may help determine what happened and how to respond",
      "It makes all malware harmless",
      "It prevents every future attack",
      "It replaces backups"
    ],
    "options_hi": [
      "यह यह निर्धारित करने में मदद कर सकता है कि क्या हुआ और कैसे सही प्रतिक्रिया दी जाए",
      "यह सभी मैलवेयर को हानिरहित बनाता है",
      "यह हर भविष्य के हमले को रोकता है",
      "यह बैकअप की जगह लेता है"
    ],
    "answer": "It may help determine what happened and how to respond",
    "correctAnswerIndex": 0,
    "explanation": "Forensic evidence (disk dumps, memory captures) proves how the breach occurred and identifies affected systems.",
    "explanation_en": "It may help determine what happened and how to respond.",
    "explanation_hi": "साक्ष्य सुरक्षित रखने से पता चलता है कि हमलावर ने किस रास्ते से प्रवेश किया और क्या डेटा चुराया।"
  },
  {
    "id": "L5_T3_SCH_06",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "Who should handle major security incidents in an organization?",
    "question_en": "Who should handle major security incidents in an organization?",
    "question_hi": "किसी संगठन में बड़ी सुरक्षा घटनाओं को किसे संभालना चाहिए?",
    "options": [
      "Authorized responders following the incident plan",
      "Any anonymous online commenter",
      "Every visitor",
      "No one"
    ],
    "options_en": [
      "Authorized responders following the incident plan",
      "Any anonymous online commenter",
      "Every visitor",
      "No one"
    ],
    "options_hi": [
      "घटना योजना (Incident Plan) का पालन करने वाले अधिकृत उत्तरदाता (IT/सुरक्षा टीम)",
      "कोई भी अनाम ऑनलाइन टिप्पणीकार",
      "हर आगंतुक",
      "कोई नहीं"
    ],
    "answer": "Authorized responders following the incident plan",
    "correctAnswerIndex": 0,
    "explanation": "Designated Computer Incident Response Teams (CIRT) are trained to coordinate containment and legal requirements.",
    "explanation_en": "Authorized responders following the incident plan.",
    "explanation_hi": "गंभीर हमलों से निपटने का काम केवल अधिकृत साइबर सुरक्षा विशेषज्ञों और प्रशिक्षित टीम को ही करना चाहिए।"
  },
  {
    "id": "L5_T3_SCH_07",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "What should happen if an account is believed to be compromised?",
    "question_en": "What should happen if an account is believed to be compromised?",
    "question_hi": "यदि किसी खाते के हैक होने का संदेह हो, तो क्या किया जाना चाहिए?",
    "options": [
      "Secure it using the approved process and report the incident",
      "Share its password with friends",
      "Ignore unusual activity",
      "Post its recovery codes online"
    ],
    "options_en": [
      "Secure it using the approved process and report the incident",
      "Share its password with friends",
      "Ignore unusual activity",
      "Post its recovery codes online"
    ],
    "options_hi": [
      "स्वीकृत प्रक्रिया का उपयोग करके इसे सुरक्षित (पासवर्ड रीसेट/सत्र समाप्त) करें और घटना की रिपोर्ट करें",
      "दोस्तों के साथ इसका पासवर्ड साझा करें",
      "असामान्य गतिविधि को अनदेखा करें",
      "इसके रिकवरी कोड ऑनलाइन पोस्ट करें"
    ],
    "answer": "Secure it using the approved process and report the incident",
    "correctAnswerIndex": 0,
    "explanation": "Immediately terminate active sessions, change credentials, and report the compromise to security teams.",
    "explanation_en": "Secure it using the approved process and report the incident.",
    "explanation_hi": "खाता हैक होने पर तुरंत पासवर्ड बदलें, सभी डिवाइस से लॉग आउट करें और IT टीम को सूचित करें।"
  },
  {
    "id": "L5_T3_SCH_08",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "Why may an affected device be disconnected from a network?",
    "question_en": "Why may an affected device be disconnected from a network?",
    "question_hi": "संक्रमित डिवाइस को नेटवर्क से अलग (Disconnect) क्यों किया जाता है?",
    "options": [
      "To help limit possible spread, if instructed by the response procedure",
      "To make all data public",
      "To guarantee no evidence remains",
      "To remove the need for investigation"
    ],
    "options_en": [
      "To help limit possible spread, if instructed by the response procedure",
      "To make all data public",
      "To guarantee no evidence remains",
      "To remove the need for investigation"
    ],
    "options_hi": [
      "यदि प्रतिक्रिया प्रक्रिया द्वारा निर्देशित किया गया हो, तो वायरस को अन्य कंप्यूटरों में फैलने से रोकने के लिए",
      "सभी डेटा को सार्वजनिक करने के लिए",
      "यह गारंटी देने के लिए कि कोई सबूत न बचे",
      "जांच की आवश्यकता को समाप्त करने के लिए"
    ],
    "answer": "To help limit possible spread, if instructed by the response procedure",
    "correctAnswerIndex": 0,
    "explanation": "Network isolation isolates infected hosts, severing command-and-control channels and worm propagation.",
    "explanation_en": "To help limit possible spread, if instructed by the response procedure.",
    "explanation_hi": "केबल या वाई-फ़ाई बंद करने से वायरस नेटवर्क के बाकी हिस्सों में फैल नहीं पाता और हैकर का संपर्क टूट जाता है।"
  },
  {
    "id": "L5_T3_SCH_09",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "Should a student try to investigate a serious attack by guessing passwords?",
    "question_en": "Should a student try to investigate a serious attack by guessing passwords?",
    "question_hi": "क्या किसी छात्र को पासवर्ड का अनुमान लगाकर किसी गंभीर हमले की स्वयं जांच करने की कोशिश करनी चाहिए?",
    "options": [
      "Yes, always",
      "No, report it and let authorized staff investigate",
      "Only on another student's account",
      "Only after posting online"
    ],
    "options_en": [
      "Yes, always",
      "No, report it and let authorized staff investigate",
      "Only on another student's account",
      "Only after posting online"
    ],
    "options_hi": [
      "हाँ, हमेशा",
      "नहीं, इसकी तुरंत सूचना दें और अधिकृत तकनीकी कर्मचारियों को जांच करने दें",
      "केवल दूसरे छात्र के खाते पर",
      "केवल ऑनलाइन पोस्ट करने के बाद"
    ],
    "answer": "No, report it and let authorized staff investigate",
    "correctAnswerIndex": 1,
    "explanation": "Unauthorized investigation or probing can destroy digital evidence and violate acceptable use policies.",
    "explanation_en": "No, report it and let authorized staff investigate.",
    "explanation_hi": "छात्रों को खुद हैकिंग की कोशिश नहीं करनी चाहिए, बल्कि तुरंत शिक्षक या IT विभाग को बताना चाहिए।"
  },
  {
    "id": "L5_T3_SCH_10",
    "level": 5,
    "topic": "Responsive Resilience",
    "topicId": "responsive_resilience",
    "mode": "school",
    "question": "What is an incident-response plan?",
    "question_en": "What is an incident-response plan?",
    "question_hi": "घटना-प्रतिक्रिया योजना (Incident Response Plan) क्या है?",
    "options": [
      "A documented guide for handling security incidents",
      "A list of public passwords",
      "A computer game",
      "A screen saver"
    ],
    "options_en": [
      "A documented guide for handling security incidents",
      "A list of public passwords",
      "A computer game",
      "A screen saver"
    ],
    "options_hi": [
      "सुरक्षा घटनाओं और हमलों से निपटने के लिए एक व्यवस्थित लिखित मार्गदर्शिका (गाइड)",
      "सार्वजनिक पासवर्ड की एक सूची",
      "एक कंप्यूटर गेम",
      "एक स्क्रीन सेवर"
    ],
    "answer": "A documented guide for handling security incidents",
    "correctAnswerIndex": 0,
    "explanation": "An incident-response plan outlines defined phases (preparation, detection, containment, eradication, recovery, post-mortem).",
    "explanation_en": "A documented guide for handling security incidents.",
    "explanation_hi": "यह एक लिखित योजना होती है जिसमें बताया होता है कि साइबर हमला होने पर किसे क्या कदम उठाने हैं।"
  },

  # Topic 24 (L5 T4): Recovery Resilience
  {
    "id": "L5_T4_SCH_01",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "What is the goal of recovery after a cyber incident?",
    "question_en": "What is the goal of recovery after a cyber incident?",
    "question_hi": "साइबर घटना के बाद पुनर्प्राप्ति (Recovery) का मुख्य लक्ष्य क्या है?",
    "options": [
      "Restore systems and data safely to normal operation",
      "Bring infected files online immediately",
      "Delete every backup",
      "Share passwords publicly"
    ],
    "options_en": [
      "Restore systems and data safely to normal operation",
      "Bring infected files online immediately",
      "Delete every backup",
      "Share passwords publicly"
    ],
    "options_hi": [
      "सिस्टम और डेटा को सुरक्षित रूप से सामान्य और सुचारू संचालन में वापस लाना",
      "संक्रमित फ़ाइलों को तुरंत ऑनलाइन लाना",
      "हर बैकअप को हटाना",
      "पासवर्ड सार्वजनिक रूप से साझा करना"
    ],
    "answer": "Restore systems and data safely to normal operation",
    "correctAnswerIndex": 0,
    "explanation": "Recovery aims to restore integrity, validate clean configurations, and bring business operations safely back online.",
    "explanation_en": "Restore systems and data safely to normal operation.",
    "explanation_hi": "पुनर्प्राप्ति का लक्ष्य प्रभावित कंप्यूटरों और डेटा को सुरक्षित तरीके से दोबारा चालू करना है।"
  },
  {
    "id": "L5_T4_SCH_02",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Why should a backup be checked before restoring it?",
    "question_en": "Why should a backup be checked before restoring it?",
    "question_hi": "बैकअप को पुनर्स्थापित (Restore) करने से पहले उसकी जांच क्यों की जानी चाहिए?",
    "options": [
      "It may be outdated or infected, so it should be verified",
      "It must always be public",
      "It replaces all security controls",
      "It makes updates unnecessary"
    ],
    "options_en": [
      "It may be outdated or infected, so it should be verified",
      "It must always be public",
      "It replaces all security controls",
      "It makes updates unnecessary"
    ],
    "options_hi": [
      "यह पुराना या मैलवेयर से संक्रमित हो सकता है, इसलिए इसे सत्यापित किया जाना चाहिए",
      "इसे हमेशा सार्वजनिक होना चाहिए",
      "यह सभी सुरक्षा नियंत्रणों की जगह लेता है",
      "यह अपडेट को अनावश्यक बनाता है"
    ],
    "answer": "It may be outdated or infected, so it should be verified",
    "correctAnswerIndex": 0,
    "explanation": "Scanning backups ensures you do not inadvertently re-infect production systems with pre-existing malware.",
    "explanation_en": "It may be outdated or infected, so it should be verified.",
    "explanation_hi": "यदि बैकअप में भी वायरस छिपा हो, तो उसे बिना जांचे रीस्टोर करने से सिस्टम फिर से संक्रमित हो सकता है।"
  },
  {
    "id": "L5_T4_SCH_03",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Why test backup restoration before an emergency?",
    "question_en": "Why test backup restoration before an emergency?",
    "question_hi": "आपातकाल से पहले ही बैकअप पुनर्स्थापना का परीक्षण (Backup Testing) क्यों करना चाहिए?",
    "options": [
      "To confirm the organization can recover the data",
      "To make passwords weaker",
      "To stop all monitoring",
      "To share private files"
    ],
    "options_en": [
      "To confirm the organization can recover the data",
      "To make passwords weaker",
      "To stop all monitoring",
      "To share private files"
    ],
    "options_hi": [
      "यह पुष्टि करने के लिए कि संकट आने पर संगठन वास्तव में डेटा को सफलतापूर्वक पुनः प्राप्त कर सकता है",
      "पासवर्ड को कमजोर बनाने के लिए",
      "सभी निगरानी रोकने के लिए",
      "निजी फ़ाइलें साझा करने के लिए"
    ],
    "answer": "To confirm the organization can recover the data",
    "correctAnswerIndex": 0,
    "explanation": "Testing validates recovery time objectives (RTO) and ensures backup media is not corrupt.",
    "explanation_en": "To confirm the organization can recover the data.",
    "explanation_hi": "पहले से परीक्षण करने से यह भरोसा मिलता है कि असली हमले के समय बैकअप बिना किसी त्रुटि के काम करेगा।"
  },
  {
    "id": "L5_T4_SCH_04",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "What should happen before a recovered system is returned to service?",
    "question_en": "What should happen before a recovered system is returned to service?",
    "question_hi": "पुनर्प्राप्त सिस्टम को दोबारा सेवा में वापस लाने से पहले क्या किया जाना चाहिए?",
    "options": [
      "Check that it is safe and apply required fixes",
      "Ignore the cause of the incident",
      "Disable all access controls",
      "Delete all logs"
    ],
    "options_en": [
      "Check that it is safe and apply required fixes",
      "Ignore the cause of the incident",
      "Disable all access controls",
      "Delete all logs"
    ],
    "options_hi": [
      "जांचें कि यह पूरी तरह सुरक्षित है और सभी आवश्यक सुरक्षा पैच और सुधार लागू करें",
      "घटना के कारण को अनदेखा करें",
      "सभी एक्सेस नियंत्रण अक्षम करें",
      "सभी लॉग्स को हटा दें"
    ],
    "answer": "Check that it is safe and apply required fixes",
    "correctAnswerIndex": 0,
    "explanation": "Recommissioning requires patching the initial vulnerability, verifying integrity, and continuous monitoring.",
    "explanation_en": "Check that it is safe and apply required fixes.",
    "explanation_hi": "सिस्टम को दोबारा चालू करने से पहले यह पक्का करना ज़रूरी है कि जिस कमज़ोरी से हमला हुआ था, उसे ठीक कर दिया गया है।"
  },
  {
    "id": "L5_T4_SCH_05",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Why keep more than one suitable backup copy?",
    "question_en": "Why keep more than one suitable backup copy?",
    "question_hi": "एक से अधिक बैकअप प्रतियां (Copies) रखना क्यों समझदारी है?",
    "options": [
      "One copy may be lost, damaged, or affected by an incident",
      "It makes phishing impossible",
      "It removes the need for updates",
      "It makes every file public"
    ],
    "options_en": [
      "One copy may be lost, damaged, or affected by an incident",
      "It makes phishing impossible",
      "It removes the need for updates",
      "It makes every file public"
    ],
    "options_hi": [
      "एक प्रति खो सकती है, क्षतिग्रस्त हो सकती है या हमले से प्रभावित हो सकती है (3-2-1 बैकअप नियम)",
      "यह फ़िशिंग को असंभव बनाता है",
      "यह अपडेट की आवश्यकता को समाप्त करता है",
      "यह हर फ़ाइल को सार्वजनिक बनाता है"
    ],
    "answer": "One copy may be lost, damaged, or affected by an incident",
    "correctAnswerIndex": 0,
    "explanation": "The 3-2-1 backup strategy protects against localized disasters and ransomware encrypting local drives.",
    "explanation_en": "One copy may be lost, damaged, or affected by an incident.",
    "explanation_hi": "यदि एक बैकअप खराब हो जाए या आग लग जाए, तो दूसरी ऑफ़लाइन या क्लाउड कॉपी से डेटा बचाया जा सकता है।"
  },
  {
    "id": "L5_T4_SCH_06",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "What is one useful activity after recovery?",
    "question_en": "What is one useful activity after recovery?",
    "question_hi": "पुनर्प्राप्ति (Recovery) पूरी होने के बाद एक उपयोगी गतिविधि क्या है?",
    "options": [
      "Review the incident and improve weak controls",
      "Forget the incident without learning",
      "Publish administrator credentials",
      "Stop making backups"
    ],
    "options_en": [
      "Review the incident and improve weak controls",
      "Forget the incident without learning",
      "Publish administrator credentials",
      "Stop making backups"
    ],
    "options_hi": [
      "घटना की समीक्षा करना और कमजोर सुरक्षा नियंत्रणों में सुधार करना (Lessons Learned)",
      "बिना कुछ सीखे घटना को भूल जाना",
      "व्यवस्थापक क्रेडेंशियल प्रकाशित करना",
      "बैकअप बनाना बंद करना"
    ],
    "answer": "Review the incident and improve weak controls",
    "correctAnswerIndex": 0,
    "explanation": "Post-recovery reviews document root causes to prevent repeat security compromises.",
    "explanation_en": "Review the incident and improve weak controls.",
    "explanation_hi": "घटना से सीखकर अपनी सुरक्षा कमज़ोरियों को दूर करना भविष्य के हमलों से बचाव का सबसे अच्छा तरीका है।"
  },
  {
    "id": "L5_T4_SCH_07",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Who should approve the restoration of critical school systems?",
    "question_en": "Who should approve the restoration of critical school systems?",
    "question_hi": "महत्वपूर्ण स्कूल प्रणालियों की पुनर्स्थापना को किसे मंजूरी देनी चाहिए?",
    "options": [
      "Authorized IT staff or responsible administrators",
      "Any student online",
      "An unknown caller",
      "A public social media poll"
    ],
    "options_en": [
      "Authorized IT staff or responsible administrators",
      "Any student online",
      "An unknown caller",
      "A public social media poll"
    ],
    "options_hi": [
      "अधिकृत IT कर्मचारी या जिम्मेदार स्कूल प्रशासक",
      "कोई भी छात्र ऑनलाइन",
      "एक अज्ञात कॉलर",
      "सार्वजनिक सोशल मीडिया पोल"
    ],
    "answer": "Authorized IT staff or responsible administrators",
    "correctAnswerIndex": 0,
    "explanation": "Bringing core infrastructure back online requires verification and sign-off by designated authorities.",
    "explanation_en": "Authorized IT staff or responsible administrators.",
    "explanation_hi": "सिस्टम पूरी तरह साफ़ और सुरक्षित है, इसकी पुष्टि केवल अधिकृत IT अधिकारी ही कर सकते हैं।"
  },
  {
    "id": "L5_T4_SCH_08",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Why is a recovery plan important?",
    "question_en": "Why is a recovery plan important?",
    "question_hi": "एक पुनर्प्राप्ति योजना (Recovery Plan) क्यों महत्वपूर्ण है?",
    "options": [
      "It clarifies how to restore important services after disruption",
      "It guarantees that nothing can go wrong",
      "It removes all user accounts",
      "It replaces incident detection"
    ],
    "options_en": [
      "It clarifies how to restore important services after disruption",
      "It guarantees that nothing can go wrong",
      "It removes all user accounts",
      "It replaces incident detection"
    ],
    "options_hi": [
      "यह स्पष्ट करती है कि किसी बड़ी रुकावट या हमले के बाद महत्वपूर्ण सेवाओं को कैसे दोबारा बहाल किया जाए",
      "यह गारंटी देती है कि कुछ भी गलत नहीं हो सकता",
      "यह सभी उपयोगकर्ता खातों को हटाती है",
      "यह घटना पहचान की जगह लेती है"
    ],
    "answer": "It clarifies how to restore important services after disruption",
    "correctAnswerIndex": 0,
    "explanation": "A documented plan eliminates panic and provides step-by-step instructions for system rebuilds.",
    "explanation_en": "It clarifies how to restore important services after disruption.",
    "explanation_hi": "योजना होने से आपातकाल में बिना घबराए क्रमबद्ध तरीके से स्कूल के सिस्टम को बहाल किया जा सकता है।"
  },
  {
    "id": "L5_T4_SCH_09",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "What is a clean backup?",
    "question_en": "What is a clean backup?",
    "question_hi": "एक 'स्वच्छ बैकअप' (Clean Backup) क्या होता है?",
    "options": [
      "A backup believed to be free from the incident's harmful content",
      "A backup with a short filename",
      "A backup shared publicly",
      "A backup that was never tested"
    ],
    "options_en": [
      "A backup believed to be free from the incident's harmful content",
      "A backup with a short filename",
      "A backup shared publicly",
      "A backup that was never tested"
    ],
    "options_hi": [
      "एक ऐसा बैकअप जिसे दुर्भावनापूर्ण कोड, मैलवेयर या हमले की सामग्री से पूरी तरह मुक्त माना जाता है",
      "छोटे फ़ाइल नाम वाला बैकअप",
      "सार्वजनिक रूप से साझा किया गया बैकअप",
      "एक बैकअप जिसका कभी परीक्षण नहीं किया गया"
    ],
    "answer": "A backup believed to be free from the incident's harmful content",
    "correctAnswerIndex": 0,
    "explanation": "Clean backups represent pristine snapshots captured before the adversary gained initial access.",
    "explanation_en": "A backup believed to be free from the incident's harmful content.",
    "explanation_hi": "स्वच्छ बैकअप वह प्रति है जो हमले से पहले की तारीख की होती है और जिसमें कोई वायरस नहीं होता।"
  },
  {
    "id": "L5_T4_SCH_10",
    "level": 5,
    "topic": "Recovery Resilience",
    "topicId": "recovery_resilience",
    "mode": "school",
    "question": "Should an organization fix the weakness that caused an incident?",
    "question_en": "Should an organization fix the weakness that caused an incident?",
    "question_hi": "क्या किसी संगठन को उस कमज़ोरी को ठीक करना चाहिए जिसके कारण घटना घटी थी?",
    "options": [
      "Yes, where possible before or during safe recovery",
      "No, the same weakness should remain",
      "Only if the wallpaper changes",
      "Only after deleting all records"
    ],
    "options_en": [
      "Yes, where possible before or during safe recovery",
      "No, the same weakness should remain",
      "Only if the wallpaper changes",
      "Only after deleting all records"
    ],
    "options_hi": [
      "हाँ, सुरक्षित पुनर्प्राप्ति के दौरान या उससे पहले जहाँ तक संभव हो उस कमज़ोरी को पैच/ठीक किया जाना चाहिए",
      "नहीं, वही कमज़ोरी बनी रहनी चाहिए",
      "केवल तभी जब वॉलपेपर बदल जाए",
      "केवल सभी रिकॉर्ड हटाने के बाद"
    ],
    "answer": "Yes, where possible before or during safe recovery",
    "correctAnswerIndex": 0,
    "explanation": "Failing to patch the root cause leaves systems vulnerable to re-infection by the same threat actor.",
    "explanation_en": "Yes, where possible before or during safe recovery.",
    "explanation_hi": "यदि मूल कमज़ोरी ठीक नहीं की गई तो हैकर दोबारा उसी रास्ते से अंदर घुसकर फिर हमला कर देगा।"
  },

  # Topic 25 (L5 T5): Adaptive (Evolving) Resilience
  {
    "id": "L5_T5_SCH_01",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "What does adaptive cyber resilience mean?",
    "question_en": "What does adaptive cyber resilience mean?",
    "question_hi": "अनुकूली साइबर लचीलापन (Adaptive Cyber Resilience) का क्या अर्थ है?",
    "options": [
      "Learning and adjusting defenses as threats and systems change",
      "Never changing security rules",
      "Using only one password forever",
      "Ignoring new risks"
    ],
    "options_en": [
      "Learning and adjusting defenses as threats and systems change",
      "Never changing security rules",
      "Using only one password forever",
      "Ignoring new risks"
    ],
    "options_hi": [
      "खतरों, तकनीकों और प्रणालियों के बदलने के साथ-साथ अपनी सुरक्षा को लगातार सीखना और अनुकूलित करना",
      "सुरक्षा नियमों को कभी न बदलना",
      "हमेशा केवल एक पासवर्ड का उपयोग करना",
      "नए जोखिमों को अनदेखा करना"
    ],
    "answer": "Learning and adjusting defenses as threats and systems change",
    "correctAnswerIndex": 0,
    "explanation": "Adaptive resilience proactively evolves security posture based on emerging threats and operational changes.",
    "explanation_en": "Learning and adjusting defenses as threats and systems change.",
    "explanation_hi": "साइबर खतरे हमेशा बदलते रहते हैं, इसलिए अपनी सुरक्षा रणनीतियों को भी लगातार अपडेट और विकसित करना चाहिए।"
  },
  {
    "id": "L5_T5_SCH_02",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "Why should an organization review its security after an incident?",
    "question_en": "Why should an organization review its security after an incident?",
    "question_hi": "किसी सुरक्षा घटना के बाद संगठन को अपनी सुरक्षा की समीक्षा क्यों करनी चाहिए?",
    "options": [
      "To learn what worked and what needs improvement",
      "To hide every mistake",
      "To publish private data",
      "To remove all monitoring"
    ],
    "options_en": [
      "To learn what worked and what needs improvement",
      "To hide every mistake",
      "To publish private data",
      "To remove all monitoring"
    ],
    "options_hi": [
      "यह सीखने के लिए कि क्या उपाय सफल रहे और कहाँ सुधार की आवश्यकता है",
      "हर गलती को छिपाने के लिए",
      "निजी डेटा प्रकाशित करने के लिए",
      "सभी निगरानी हटाने के लिए"
    ],
    "answer": "To learn what worked and what needs improvement",
    "correctAnswerIndex": 0,
    "explanation": "Post-incident analysis reveals gaps in architecture, detection rules, and training.",
    "explanation_en": "To learn what worked and what needs improvement.",
    "explanation_hi": "समीक्षा करने से यह साफ होता है कि हमारी सुरक्षा में क्या कमी रह गई थी और उसे कैसे सुधारा जाए।"
  },
  {
    "id": "L5_T5_SCH_03",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "A new scam is targeting students. What is a useful adaptive response?",
    "question_en": "A new scam is targeting students. What is a useful adaptive response?",
    "question_hi": "छात्रों को निशाना बनाने वाला एक नया ऑनलाइन घोटाला सामने आया है। एक उपयोगी अनुकूली प्रतिक्रिया क्या है?",
    "options": [
      "Update awareness guidance to explain the new warning signs",
      "Keep old advice unchanged forever",
      "Encourage students to click the scam",
      "Share account passwords"
    ],
    "options_en": [
      "Update awareness guidance to explain the new warning signs",
      "Keep old advice unchanged forever",
      "Encourage students to click the scam",
      "Share account passwords"
    ],
    "options_hi": [
      "नए चेतावनी संकेतों और बचने के तरीकों को समझाने के लिए जागरूकता दिशा-निर्देशों को तुरंत अपडेट करना",
      "पुरानी सलाह को हमेशा के लिए अपरिवर्तित रखना",
      "छात्रों को घोटाले वाले लिंक पर क्लिक करने के लिए प्रोत्साहित करना",
      "खाते के पासवर्ड साझा करना"
    ],
    "answer": "Update awareness guidance to explain the new warning signs",
    "correctAnswerIndex": 0,
    "explanation": "Rapidly updating awareness advisories counters new social engineering tricks and prevents victimhood.",
    "explanation_en": "Update awareness guidance to explain the new warning signs.",
    "explanation_hi": "नए घोटालों के आते ही छात्रों को उनके तौर-तरीकों से आगाह करना अनुकूली सुरक्षा का सबसे अच्छा उदाहरण है।"
  },
  {
    "id": "L5_T5_SCH_04",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "Why test a response plan periodically?",
    "question_en": "Why test a response plan periodically?",
    "question_hi": "प्रतिक्रिया योजना (Response Plan) का समय-समय पर परीक्षण क्यों किया जाना चाहिए?",
    "options": [
      "To find gaps before a real emergency",
      "To guarantee no incident will happen",
      "To make all data public",
      "To remove the need for staff"
    ],
    "options_en": [
      "To find gaps before a real emergency",
      "To guarantee no incident will happen",
      "To make all data public",
      "To remove the need for staff"
    ],
    "options_hi": [
      "वास्तविक आपातकाल आने से पहले सुरक्षा कमियों और कमज़ोरियों को खोजने के लिए",
      "यह गारंटी देने के लिए कि कोई घटना कभी नहीं होगी",
      "सभी डेटा को सार्वजनिक करने के लिए",
      "कर्मचारियों की आवश्यकता को समाप्त करने के लिए"
    ],
    "answer": "To find gaps before a real emergency",
    "correctAnswerIndex": 0,
    "explanation": "Simulations identify outdated phone trees, obsolete tooling, and unpatched access paths.",
    "explanation_en": "To find gaps before a real emergency.",
    "explanation_hi": "नियमित अभ्यास से पता चलता है कि वास्तविक संकट में कौन सा कदम ठीक से काम नहीं कर रहा था।"
  },
  {
    "id": "L5_T5_SCH_05",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "What can lessons learned from an incident help improve?",
    "question_en": "What can lessons learned from an incident help improve?",
    "question_hi": "किसी सुरक्षा घटना से सीखे गए सबक (Lessons Learned) क्या सुधारने में मदद कर सकते हैं?",
    "options": [
      "Training, processes, and technical safeguards",
      "Only screen brightness",
      "Public password lists",
      "Unrestricted access"
    ],
    "options_en": [
      "Training, processes, and technical safeguards",
      "Only screen brightness",
      "Public password lists",
      "Unrestricted access"
    ],
    "options_hi": [
      "प्रशिक्षण, सुरक्षा नीतियां और तकनीकी सुरक्षा उपाय (फ़ायरवॉल/सॉफ़्टवेयर)",
      "केवल स्क्रीन की चमक",
      "सार्वजनिक पासवर्ड सूचियाँ",
      "अप्रतिबंधित खुली पहुँच"
    ],
    "answer": "Training, processes, and technical safeguards",
    "correctAnswerIndex": 0,
    "explanation": "Feedback loops convert incident lessons into stronger policies, enhanced telemetry, and targeted user training.",
    "explanation_en": "Training, processes, and technical safeguards.",
    "explanation_hi": "पुरानी गलतियों से सीखकर कर्मचारियों के प्रशिक्षण, सुरक्षा नियमों और एंटीवायरस सेटिंग्स को और मजबूत किया जाता है।"
  },
  {
    "id": "L5_T5_SCH_06",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "Why should cybersecurity controls be reviewed when technology changes?",
    "question_en": "Why should cybersecurity controls be reviewed when technology changes?",
    "question_hi": "जब नई तकनीक अपनाई जाती है तो साइबर सुरक्षा नियंत्रणों की समीक्षा क्यों की जानी चाहिए?",
    "options": [
      "New systems may introduce new risks",
      "New technology is always perfectly safe",
      "Updates never affect security",
      "Passwords no longer matter"
    ],
    "options_en": [
      "New systems may introduce new risks",
      "New technology is always perfectly safe",
      "Updates never affect security",
      "Passwords no longer matter"
    ],
    "options_hi": [
      "नई प्रणालियां और नए उपकरण नए सुरक्षा जोखिम और कमज़ोरियाँ ला सकते हैं",
      "नई तकनीक हमेशा पूरी तरह से सुरक्षित होती है",
      "अपडेट कभी सुरक्षा को प्रभावित नहीं करते",
      "पासवर्ड अब कोई मायने नहीं रखते"
    ],
    "answer": "New systems may introduce new risks",
    "correctAnswerIndex": 0,
    "explanation": "New cloud tools, APIs, and connected IoT devices expand the perimeter and require updated security standards.",
    "explanation_en": "New systems may introduce new risks.",
    "explanation_hi": "जब भी कोई नया सॉफ़्टवेयर या डिवाइस नेटवर्क से जुड़ता है, तो उसके साथ नए खतरे भी आ सकते हैं जिनकी जांच ज़रूरी है।"
  },
  {
    "id": "L5_T5_SCH_07",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "What is continuous improvement?",
    "question_en": "What is continuous improvement?",
    "question_hi": "निरंतर सुधार (Continuous Improvement) क्या है?",
    "options": [
      "Making repeated changes based on evidence and results",
      "Never reviewing a process",
      "Deleting all feedback",
      "Allowing every connection"
    ],
    "options_en": [
      "Making repeated changes based on evidence and results",
      "Never reviewing a process",
      "Deleting all feedback",
      "Allowing every connection"
    ],
    "options_hi": [
      "प्रमाण, डेटा और सुरक्षा परिणामों के आधार पर लगातार सकारात्मक बदलाव और सुधार करना",
      "किसी प्रक्रिया की कभी समीक्षा न करना",
      "सभी फीडबैक को हटा देना",
      "हर कनेक्शन की अनुमति देना"
    ],
    "answer": "Making repeated changes based on evidence and results",
    "correctAnswerIndex": 0,
    "explanation": "Continuous improvement relies on iterative measurement, metrics, and tuning to continually advance maturity.",
    "explanation_en": "Making repeated changes based on evidence and results.",
    "explanation_hi": "सुरक्षा एक बार का काम नहीं है; सुरक्षा ऑडिट और नए खतरों के आधार पर लगातार सुधार करते रहना ही निरंतर सुधार है।"
  },
  {
    "id": "L5_T5_SCH_08",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "How can feedback from users improve security?",
    "question_en": "How can feedback from users improve security?",
    "question_hi": "उपयोगकर्ताओं (छात्रों/शिक्षकों) से मिलने वाला फ़ीडबैक सुरक्षा को कैसे बेहतर बना सकता है?",
    "options": [
      "It can reveal confusing rules or problems that need fixing",
      "It makes every attack impossible",
      "It removes all access controls",
      "It automatically restores files"
    ],
    "options_en": [
      "It can reveal confusing rules or problems that need fixing",
      "It makes every attack impossible",
      "It removes all access controls",
      "It automatically restores files"
    ],
    "options_hi": [
      "यह भ्रमित करने वाले नियमों, उपयोगिता समस्याओं या अनजाने सुरक्षा जोखिमों को उजागर कर सकता है",
      "यह हर हमले को असंभव बना देता है",
      "यह सभी एक्सेस नियंत्रण हटा देता है",
      "यह फ़ाइलों को स्वचालित रूप से पुनर्स्थापित करता है"
    ],
    "answer": "It can reveal confusing rules or problems that need fixing",
    "correctAnswerIndex": 0,
    "explanation": "User feedback highlights friction where overly restrictive rules inadvertently encourage unsafe workarounds.",
    "explanation_en": "It can reveal confusing rules or problems that need fixing.",
    "explanation_hi": "यदि सुरक्षा नियम बहुत जटिल हों तो छात्र बाईपास ढूंढने लगते हैं; फ़ीडबैक से नियमों को व्यावहारिक और सुरक्षित बनाया जा सकता है।"
  },
  {
    "id": "L5_T5_SCH_09",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "What should a team do after discovering a repeated security weakness?",
    "question_en": "What should a team do after discovering a repeated security weakness?",
    "question_hi": "बार-बार सामने आने वाली किसी सुरक्षा कमज़ोरी का पता चलने पर टीम को क्या करना चाहिए?",
    "options": [
      "Investigate the cause and improve the control or process",
      "Ignore it",
      "Post credentials online",
      "Turn off all security"
    ],
    "options_en": [
      "Investigate the cause and improve the control or process",
      "Ignore it",
      "Post credentials online",
      "Turn off all security"
    ],
    "options_hi": [
      "मूल कारण की जांच करें और सुरक्षा नियंत्रण या प्रक्रिया को स्थायी रूप से सुधारें",
      "इसे अनदेखा करें",
      "क्रेडेंशियल ऑनलाइन पोस्ट करें",
      "सभी सुरक्षा बंद कर दें"
    ],
    "answer": "Investigate the cause and improve the control or process",
    "correctAnswerIndex": 0,
    "explanation": "Persistent vulnerabilities indicate architectural or systemic procedural gaps requiring foundational fixes.",
    "explanation_en": "Investigate the cause and improve the control or process.",
    "explanation_hi": "यदि कोई गलती बार-बार हो रही है, तो उसके मूल कारण की जांच करके प्रक्रिया को बदलना चाहिए ताकि वह दोबारा न हो।"
  },
  {
    "id": "L5_T5_SCH_10",
    "level": 5,
    "topic": "Adaptive (Evolving) Resilience",
    "topicId": "adaptive_evolving_resilience",
    "mode": "school",
    "question": "Which best describes a resilient organization?",
    "question_en": "Which best describes a resilient organization?",
    "question_hi": "एक साइबर-लचीले संगठन (Resilient Organization) का सबसे अच्छा वर्णन कौन सा है?",
    "options": [
      "It prepares for incidents, responds, recovers, and learns",
      "It assumes incidents are impossible",
      "It never makes backups",
      "It gives everyone full access"
    ],
    "options_en": [
      "It prepares for incidents, responds, recovers, and learns",
      "It assumes incidents are impossible",
      "It never makes backups",
      "It gives everyone full access"
    ],
    "options_hi": [
      "जो घटनाओं के लिए तैयारी करता है, त्वरित प्रतिक्रिया देता है, सुरक्षित पुनर्प्राप्ति करता है और लगातार सीखता है",
      "जो मानता है कि साइबर हमले असंभव हैं",
      "जो कभी बैकअप नहीं बनाता",
      "जो सभी को पूर्ण खुली पहुँच देता है"
    ],
    "answer": "It prepares for incidents, responds, recovers, and learns",
    "correctAnswerIndex": 0,
    "explanation": "Cyber resilience is a continuous lifecycle: anticipate, withstand, recover from, and adapt to attacks.",
    "explanation_en": "It prepares for incidents, responds, recovers, and learns.",
    "explanation_hi": "साइबर लचीलेपन का मूल मंत्र है: पहले से तैयारी, संकट में त्वरित प्रतिक्रिया, शीघ्र बहाली और भविष्य के लिए सीखना।"
  }
]

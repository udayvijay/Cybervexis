# -*- coding: utf-8 -*-
"""Level 3: SOC (Security Operations Center) (5 topics x 10 questions = 50 questions)"""

level3_questions = [
  # Topic 11 (L3 T1): In-House SOC
  {
    "id": "L3_T1_SCH_01",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What is the main purpose of a Security Operations Centre (SOC)?",
    "question_en": "What is the main purpose of a Security Operations Centre (SOC)?",
    "question_hi": "सुरक्षा संचालन केंद्र (SOC - Security Operations Centre) का मुख्य उद्देश्य क्या है?",
    "options": [
      "Monitor, detect, investigate, and help respond to security threats",
      "Design school uniforms",
      "Manage lunch menus",
      "Repair classroom furniture"
    ],
    "options_en": [
      "Monitor, detect, investigate, and help respond to security threats",
      "Design school uniforms",
      "Manage lunch menus",
      "Repair classroom furniture"
    ],
    "options_hi": [
      "सुरक्षा खतरों की निरंतर निगरानी, पहचान, जांच और उनसे निपटने में मदद करना",
      "स्कूल की वर्दी डिजाइन करना",
      "दोपहर के भोजन के मेनू का प्रबंधन करना",
      "कक्षा के फर्नीचर की मरम्मत करना"
    ],
    "answer": "Monitor, detect, investigate, and help respond to security threats",
    "correctAnswerIndex": 0,
    "explanation": "A SOC functions as a command hub to monitor, detect, analyze, and remediate cybersecurity events 24/7.",
    "explanation_en": "A SOC functions as a command hub to monitor, detect, analyze, and remediate cybersecurity events 24/7.",
    "explanation_hi": "SOC एक केंद्रीय सुरक्षा नियंत्रण कक्ष होता है जो चौबीसों घंटे साइबर हमलों की निगरानी और बचाव करता है।"
  },
  {
    "id": "L3_T1_SCH_02",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What might a SOC analyst review to spot suspicious activity?",
    "question_en": "What might a SOC analyst review to spot suspicious activity?",
    "question_hi": "संदिग्ध गतिविधि का पता लगाने के लिए एक SOC विश्लेषक (Analyst) किसकी समीक्षा कर सकता है?",
    "options": [
      "Security alerts and system logs",
      "Only the desktop wallpaper",
      "A student's favourite song",
      "The weather forecast"
    ],
    "options_en": [
      "Security alerts and system logs",
      "Only the desktop wallpaper",
      "A student's favourite song",
      "The weather forecast"
    ],
    "options_hi": [
      "सुरक्षा चेतावनियाँ (Alerts) और सिस्टम गतिविधि लॉग्स (Logs)",
      "केवल डेस्कटॉप वॉलपेपर",
      "किसी छात्र का पसंदीदा गाना",
      "मौसम का पूर्वानुमान"
    ],
    "answer": "Security alerts and system logs",
    "correctAnswerIndex": 0,
    "explanation": "SOC analysts examine telemetry, intrusion detection alerts, and system event logs to trace breaches.",
    "explanation_en": "SOC analysts examine telemetry, intrusion detection alerts, and system event logs to trace breaches.",
    "explanation_hi": "SOC विश्लेषक कंप्यूटर नेटवर्क के लॉग्स और सुरक्षा अलर्ट्स की जांच करके हैकिंग प्रयासों को पकड़ते हैं।"
  },
  {
    "id": "L3_T1_SCH_03",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "Why does a SOC prioritize alerts?",
    "question_en": "Why does a SOC prioritize alerts?",
    "question_hi": "एक SOC चेतावनियों (Alerts) को प्राथमिकता (Priority) के अनुसार क्यों छांटता है?",
    "options": [
      "To focus attention on the most serious or urgent risks",
      "To ignore every alert",
      "To make computers louder",
      "To remove passwords"
    ],
    "options_en": [
      "To focus attention on the most serious or urgent risks",
      "To ignore every alert",
      "To make computers louder",
      "To remove passwords"
    ],
    "options_hi": [
      "सबसे गंभीर या तत्काल जोखिमों पर ध्यान केंद्रित करने के लिए",
      "प्रत्येक अलर्ट को अनदेखा करने के लिए",
      "कंप्यूटर की आवाज़ तेज़ करने के लिए",
      "पासवर्ड हटाने के लिए"
    ],
    "answer": "To focus attention on the most serious or urgent risks",
    "correctAnswerIndex": 0,
    "explanation": "Triage prioritizes high-severity incidents so critical active threats are mitigated without alert fatigue.",
    "explanation_en": "Triage prioritizes high-severity incidents so critical active threats are mitigated without alert fatigue.",
    "explanation_hi": "हजारों सामान्य सूचनाओं के बीच सबसे खतरनाक हमलों पर तुरंत ध्यान देने के लिए अलर्ट्स को प्राथमिकता दी जाती है।"
  },
  {
    "id": "L3_T1_SCH_04",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What should an analyst do when an alert looks serious?",
    "question_en": "What should an analyst do when an alert looks serious?",
    "question_hi": "जब कोई सुरक्षा अलर्ट गंभीर दिखाई दे तो विश्लेषक को क्या करना चाहिए?",
    "options": [
      "Follow the incident-response process and escalate it",
      "Delete all evidence",
      "Post confidential logs publicly",
      "Ignore it until next year"
    ],
    "options_en": [
      "Follow the incident-response process and escalate it",
      "Delete all evidence",
      "Post confidential logs publicly",
      "Ignore it until next year"
    ],
    "options_hi": [
      "घटना-प्रतिक्रिया प्रक्रिया (Incident Response) का पालन करें और इसे आगे बढ़ाएं (Escalate करें)",
      "सभी साक्ष्य मिटा दें",
      "गोपनीय लॉग्स को सार्वजनिक रूप से पोस्ट करें",
      "अगले साल तक इसे अनदेखा करें"
    ],
    "answer": "Follow the incident-response process and escalate it",
    "correctAnswerIndex": 0,
    "explanation": "Analysts follow defined SOPs to confirm indicators of compromise and escalate incidents to tier-2/lead responders.",
    "explanation_en": "Analysts follow defined SOPs to confirm indicators of compromise and escalate incidents to tier-2/lead responders.",
    "explanation_hi": "गंभीर खतरे की स्थिति में निर्धारित आपातकालीन प्रक्रिया का पालन करते हुए उच्च अधिकारियों को सूचित करना चाहिए।"
  },
  {
    "id": "L3_T1_SCH_05",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What is a false positive in security monitoring?",
    "question_en": "What is a false positive in security monitoring?",
    "question_hi": "सुरक्षा निगरानी में फ़ाल्स पॉज़िटिव (False Positive) क्या होता है?",
    "options": [
      "An alert that looks suspicious but is not an actual threat",
      "A confirmed stolen laptop",
      "A successful backup",
      "A new keyboard"
    ],
    "options_en": [
      "An alert that looks suspicious but is not an actual threat",
      "A confirmed stolen laptop",
      "A successful backup",
      "A new keyboard"
    ],
    "options_hi": [
      "एक ऐसा अलर्ट जो संदिग्ध दिखता है लेकिन वास्तव में कोई खतरा नहीं होता (झूठा अलार्म)",
      "एक पुष्ट चोरी हुआ लैपटॉप",
      "एक सफल बैकअप",
      "एक नया कीबोर्ड"
    ],
    "answer": "An alert that looks suspicious but is not an actual threat",
    "correctAnswerIndex": 0,
    "explanation": "A false positive occurs when legitimate activity triggers a security alert incorrectly.",
    "explanation_en": "A false positive occurs when legitimate activity triggers a security alert incorrectly.",
    "explanation_hi": "जब कोई सामान्य और वैध काम गलती से सुरक्षा प्रणाली द्वारा खतरे के रूप में पहचान लिया जाए, तो उसे फ़ाल्स पॉज़िटिव कहते हैं।"
  },
  {
    "id": "L3_T1_SCH_06",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "Why is teamwork important in a SOC?",
    "question_en": "Why is teamwork important in a SOC?",
    "question_hi": "SOC में टीम वर्क (आपसी तालमेल) क्यों महत्वपूर्ण है?",
    "options": [
      "Incidents may need monitoring, investigation, and response by different people",
      "It means nobody needs training",
      "It makes every alert harmless",
      "It replaces documentation"
    ],
    "options_en": [
      "Incidents may need monitoring, investigation, and response by different people",
      "It means nobody needs training",
      "It makes every alert harmless",
      "It replaces documentation"
    ],
    "options_hi": [
      "सुरक्षा घटनाओं की निगरानी, जांच और प्रतिक्रिया के लिए विभिन्न विशेषज्ञों के समन्वय की आवश्यकता होती है",
      "इसका मतलब है कि किसी को प्रशिक्षण की आवश्यकता नहीं है",
      "यह हर अलर्ट को हानिरहित बनाता है",
      "यह दस्तावेज़ीकरण की जगह लेता है"
    ],
    "answer": "Incidents may need monitoring, investigation, and response by different people",
    "correctAnswerIndex": 0,
    "explanation": "Complex cyber incidents require seamless handoffs between monitoring, forensics, and remediation teams.",
    "explanation_en": "Complex cyber incidents require seamless handoffs between monitoring, forensics, and remediation teams.",
    "explanation_hi": "साइबर हमलों से निपटने के लिए विभिन्न स्तरों के विश्लेषकों और इंजीनियरों का मिलकर काम करना आवश्यक होता है।"
  },
  {
    "id": "L3_T1_SCH_07",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "Why should SOC analysts protect log information?",
    "question_en": "Why should SOC analysts protect log information?",
    "question_hi": "SOC विश्लेषकों को लॉग जानकारी (Log Data) की सुरक्षा क्यों करनी चाहिए?",
    "options": [
      "Logs can contain sensitive details about systems and users",
      "Logs are always meant to be public",
      "Logs contain no information",
      "Logs automatically erase threats"
    ],
    "options_en": [
      "Logs can contain sensitive details about systems and users",
      "Logs are always meant to be public",
      "Logs contain no information",
      "Logs automatically erase threats"
    ],
    "options_hi": [
      "लॉग्स में सिस्टम, नेटवर्क संरचना और उपयोगकर्ताओं के बारे में संवेदनशील विवरण हो सकते हैं",
      "लॉग्स हमेशा सार्वजनिक होने के लिए होते हैं",
      "लॉग्स में कोई जानकारी नहीं होती",
      "लॉग्स स्वचालित रूप से खतरों को मिटा देते हैं"
    ],
    "answer": "Logs can contain sensitive details about systems and users",
    "correctAnswerIndex": 0,
    "explanation": "Audit logs hold internal IP addresses, user accounts, and confidential transaction details.",
    "explanation_en": "Audit logs hold internal IP addresses, user accounts, and confidential transaction details.",
    "explanation_hi": "लॉग्स में नेटवर्क और यूज़र्स का निजी डेटा होता है; यदि हैकर्स को यह मिल जाए तो वे और बड़ा हमला कर सकते हैं।"
  },
  {
    "id": "L3_T1_SCH_08",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What is a security incident?",
    "question_en": "What is a security incident?",
    "question_hi": "सुरक्षा घटना (Security Incident) क्या है?",
    "options": [
      "An event that threatens the confidentiality, integrity, or availability of systems or data",
      "A normal screen saver",
      "A planned class break",
      "A printer running out of paper"
    ],
    "options_en": [
      "An event that threatens the confidentiality, integrity, or availability of systems or data",
      "A normal screen saver",
      "A planned class break",
      "A printer running out of paper"
    ],
    "options_hi": [
      "ऐसी घटना जो सिस्टम या डेटा की गोपनीयता, अखंडता या उपलब्धता (CIA Triad) को खतरे में डालती है",
      "एक सामान्य स्क्रीन सेवर",
      "कक्षा का एक नियोजित ब्रेक",
      "प्रिंटर में कागज़ खत्म होना"
    ],
    "answer": "An event that threatens the confidentiality, integrity, or availability of systems or data",
    "correctAnswerIndex": 0,
    "explanation": "Security incidents compromise CIA triad principles through malware, unauthorized access, or sabotage.",
    "explanation_en": "Security incidents compromise CIA triad principles through malware, unauthorized access, or sabotage.",
    "explanation_hi": "कोई भी ऐसी अनपेक्षित घटना जो कंप्यूटर डेटा की चोरी, छेड़छाड़ या रुकावट पैदा करे, सुरक्षा घटना कहलाती है।"
  },
  {
    "id": "L3_T1_SCH_09",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "Why might a SOC monitor systems outside normal office hours?",
    "question_en": "Why might a SOC monitor systems outside normal office hours?",
    "question_hi": "एक SOC सामान्य कार्यालय समय के बाहर (रात या सप्ताहांत में) भी सिस्टम की निगरानी क्यों करता है?",
    "options": [
      "Attacks can happen at any time",
      "Computers only work at night",
      "It stops all software updates",
      "It makes passwords unnecessary"
    ],
    "options_en": [
      "Attacks can happen at any time",
      "Computers only work at night",
      "It stops all software updates",
      "It makes passwords unnecessary"
    ],
    "options_hi": [
      "साइबर हमले किसी भी समय, विशेषकर छुट्टियों या रात में हो सकते हैं",
      "कंप्यूटर केवल रात में काम करते हैं",
      "यह सभी सॉफ़्टवेयर अपडेट को रोकता है",
      "यह पासवर्ड को अनावश्यक बनाता है"
    ],
    "answer": "Attacks can happen at any time",
    "correctAnswerIndex": 0,
    "explanation": "Threat actors frequently launch automated and targeted strikes off-hours when IT presence is minimal.",
    "explanation_en": "Threat actors frequently launch automated and targeted strikes off-hours when IT presence is minimal.",
    "explanation_hi": "हैकर अक्सर रात या छुट्टियों के समय हमला करते हैं जब कार्यालय बंद होते हैं, इसलिए 24/7 निगरानी ज़रूरी है।"
  },
  {
    "id": "L3_T1_SCH_10",
    "level": 3,
    "topic": "In-House SOC",
    "topicId": "inhouse_soc",
    "mode": "school",
    "question": "What should a SOC do after an incident is handled?",
    "question_en": "What should a SOC do after an incident is handled?",
    "question_hi": "किसी सुरक्षा घटना से निपटने के बाद SOC को क्या करना चाहिए?",
    "options": [
      "Review what happened and identify improvements",
      "Forget the incident without records",
      "Publish all passwords",
      "Disable all monitoring"
    ],
    "options_en": [
      "Review what happened and identify improvements",
      "Forget the incident without records",
      "Publish all passwords",
      "Disable all monitoring"
    ],
    "options_hi": [
      "जो हुआ उसकी समीक्षा (Post-Mortem) करें और सुरक्षा सुधारों की पहचान करें",
      "बिना रिकॉर्ड रखे घटना को भूल जाएं",
      "सभी पासवर्ड प्रकाशित करें",
      "सभी निगरानी अक्षम करें"
    ],
    "answer": "Review what happened and identify improvements",
    "correctAnswerIndex": 0,
    "explanation": "Post-incident reviews (lessons learned) strengthen detection engineering and defensive playbooks.",
    "explanation_en": "Post-incident reviews (lessons learned) strengthen detection engineering and defensive playbooks.",
    "explanation_hi": "घटना की समीक्षा करने से पता चलता है कि भविष्य में ऐसे हमलों से कैसे बेहतर ढंग से बचा जा सकता है।"
  },

  # Topic 12 (L3 T2): Managed SOC
  {
    "id": "L3_T2_SCH_01",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "What makes a managed SOC different from an in-house SOC?",
    "question_en": "What makes a managed SOC different from an in-house SOC?",
    "question_hi": "मैनेज्ड SOC (Managed SOC) इन-हाउस SOC से किस प्रकार भिन्न है?",
    "options": [
      "An external provider delivers some or all SOC services",
      "It only works on printers",
      "It has no security analysts",
      "It never monitors alerts"
    ],
    "options_en": [
      "An external provider delivers some or all SOC services",
      "It only works on printers",
      "It has no security analysts",
      "It never monitors alerts"
    ],
    "options_hi": [
      "एक बाहरी विशेषज्ञ सेवा प्रदाता (External Provider) कुछ या सभी SOC सेवाएं प्रदान करता है",
      "यह केवल प्रिंटर पर काम करता है",
      "इसमें कोई सुरक्षा विश्लेषक नहीं होते",
      "यह कभी अलर्ट की निगरानी नहीं करता"
    ],
    "answer": "An external provider delivers some or all SOC services",
    "correctAnswerIndex": 0,
    "explanation": "A Managed SOC (MSSP) outsources monitoring and incident response to a specialized third-party vendor.",
    "explanation_en": "A Managed SOC (MSSP) outsources monitoring and incident response to a specialized third-party vendor.",
    "explanation_hi": "मैनेज्ड SOC में संगठन स्वयं टीम बनाने के बजाय किसी बाहरी सुरक्षा विशेषज्ञ कंपनी की सेवाएं लेता है।"
  },
  {
    "id": "L3_T2_SCH_02",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "Why might a small organization use a managed SOC?",
    "question_en": "Why might a small organization use a managed SOC?",
    "question_hi": "कोई छोटा संगठन या स्कूल मैनेज्ड SOC का उपयोग क्यों कर सकता है?",
    "options": [
      "It can access specialist monitoring skills without building a full team",
      "It no longer needs any security rules",
      "It can share all passwords publicly",
      "It guarantees no cyberattacks"
    ],
    "options_en": [
      "It can access specialist monitoring skills without building a full team",
      "It no longer needs any security rules",
      "It can share all passwords publicly",
      "It guarantees no cyberattacks"
    ],
    "options_hi": [
      "यह पूरी आंतरिक टीम बनाए बिना विशेषज्ञ सुरक्षा कौशल और 24/7 निगरानी प्राप्त कर सकता है",
      "इसे अब किसी सुरक्षा नियम की आवश्यकता नहीं है",
      "यह सभी पासवर्ड सार्वजनिक रूप से साझा कर सकता है",
      "यह गारंटी देता है कि कोई साइबर हमला नहीं होगा"
    ],
    "answer": "It can access specialist monitoring skills without building a full team",
    "correctAnswerIndex": 0,
    "explanation": "Managed SOCs offer 24/7 enterprise-grade monitoring capabilities cost-effectively for smaller orgs.",
    "explanation_en": "Managed SOCs offer 24/7 enterprise-grade monitoring capabilities cost-effectively for smaller orgs.",
    "explanation_hi": "अपनी अलग 24/7 टीम बनाना बहुत महंगा होता है, इसलिए बाहरी विशेषज्ञों की सेवा लेना किफायती रहता है।"
  },
  {
    "id": "L3_T2_SCH_03",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "What should an organization check before hiring a managed SOC provider?",
    "question_en": "What should an organization check before hiring a managed SOC provider?",
    "question_hi": "किसी मैनेज्ड SOC प्रदाता को नियुक्त करने से पहले संगठन को क्या जांचना चाहिए?",
    "options": [
      "Experience, service scope, privacy, and response arrangements",
      "The provider's logo colour only",
      "Whether it promises impossible results",
      "Whether it asks for public passwords"
    ],
    "options_en": [
      "Experience, service scope, privacy, and response arrangements",
      "The provider's logo colour only",
      "Whether it promises impossible results",
      "Whether it asks for public passwords"
    ],
    "options_hi": [
      "प्रदाता का अनुभव, सेवा का दायरा, डेटा गोपनीयता और घटना प्रतिक्रिया की व्यवस्था",
      "केवल प्रदाता के लोगो का रंग",
      "क्या यह असंभव परिणामों का वादा करता है",
      "क्या यह सार्वजनिक पासवर्ड मांगता है"
    ],
    "answer": "Experience, service scope, privacy, and response arrangements",
    "correctAnswerIndex": 0,
    "explanation": "Evaluate vendor compliance, SLAs, data privacy protections, and proven incident remediation skills.",
    "explanation_en": "Evaluate vendor compliance, SLAs, data privacy protections, and proven incident remediation skills.",
    "explanation_hi": "यह देखना ज़रूरी है कि कंपनी कितनी अनुभवी है, आपका डेटा सुरक्षित रखेगी या नहीं और संकट में कितनी जल्दी मदद करेगी।"
  },
  {
    "id": "L3_T2_SCH_04",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "Why must access given to an external SOC provider be limited?",
    "question_en": "Why must access given to an external SOC provider be limited?",
    "question_hi": "किसी बाहरी SOC प्रदाता को दी जाने वाली पहुँच (Access) को सीमित क्यों रखा जाना चाहिए?",
    "options": [
      "To reduce the risk of misuse or accidental exposure",
      "To make every file public",
      "To stop all logging",
      "To avoid written agreements"
    ],
    "options_en": [
      "To reduce the risk of misuse or accidental exposure",
      "To make every file public",
      "To stop all logging",
      "To avoid written agreements"
    ],
    "options_hi": [
      "दुरुपयोग या आकस्मिक डेटा रिसाव के जोखिम को कम करने के लिए",
      "हर फ़ाइल को सार्वजनिक करने के लिए",
      "सभी लॉगिंग रोकने के लिए",
      "लिखित समझौतों से बचने के लिए"
    ],
    "answer": "To reduce the risk of misuse or accidental exposure",
    "correctAnswerIndex": 0,
    "explanation": "Third-party access should follow strict least-privilege principles to limit potential supply-chain risks.",
    "explanation_en": "Third-party access should follow strict least-privilege principles to limit potential supply-chain risks.",
    "explanation_hi": "बाहरी कंपनी को केवल निगरानी के लिए आवश्यक डेटा ही दिया जाना चाहिए, ताकि संवेदनशील जानकारी सुरक्षित रहे।"
  },
  {
    "id": "L3_T2_SCH_05",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "A managed SOC reports a high-risk alert. What should the organization do?",
    "question_en": "A managed SOC reports a high-risk alert. What should the organization do?",
    "question_hi": "जब मैनेज्ड SOC किसी उच्च-जोखिम वाले अलर्ट की सूचना देता है, तो संगठन को क्या करना चाहिए?",
    "options": [
      "Follow the agreed escalation and incident-response process",
      "Ignore it because it is external",
      "Post the alert and passwords online",
      "Delete all backups"
    ],
    "options_en": [
      "Follow the agreed escalation and incident-response process",
      "Ignore it because it is external",
      "Post the alert and passwords online",
      "Delete all backups"
    ],
    "options_hi": [
      "पारस्परिक सहमति से तय की गई एस्केलेशन और घटना-प्रतिक्रिया प्रक्रिया का तुरंत पालन करें",
      "इसे अनदेखा करें क्योंकि यह बाहरी है",
      "अलर्ट और पासवर्ड ऑनलाइन पोस्ट करें",
      "सभी बैकअप हटा दें"
    ],
    "answer": "Follow the agreed escalation and incident-response process",
    "correctAnswerIndex": 0,
    "explanation": "Act immediately according to joint escalation playbooks to contain and mitigate the verified threat.",
    "explanation_en": "Act immediately according to joint escalation playbooks to contain and mitigate the verified threat.",
    "explanation_hi": "प्रदाता द्वारा गंभीर चेतावनी मिलने पर तुरंत आंतरिक IT टीम को सक्रिय करके खतरे को रोकना चाहिए।"
  },
  {
    "id": "L3_T2_SCH_06",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "What is a service-level agreement (SLA) used to clarify?",
    "question_en": "What is a service-level agreement (SLA) used to clarify?",
    "question_hi": "सर्विस-लेवल एग्रीमेंट (SLA) का उपयोग क्या स्पष्ट करने के लिए किया जाता है?",
    "options": [
      "Expected service, response times, and responsibilities",
      "A user's favourite app",
      "The size of a monitor",
      "A computer's wallpaper"
    ],
    "options_en": [
      "Expected service, response times, and responsibilities",
      "A user's favourite app",
      "The size of a monitor",
      "A computer's wallpaper"
    ],
    "options_hi": [
      "अपेक्षित सेवा स्तर, खतरे पर प्रतिक्रिया का समय (Response Time) और जिम्मेदारियां",
      "उपयोगकर्ता का पसंदीदा ऐप",
      "मॉनिटर का आकार",
      "कंप्यूटर का वॉलपेपर"
    ],
    "answer": "Expected service, response times, and responsibilities",
    "correctAnswerIndex": 0,
    "explanation": "SLAs contractually define expected uptime, incident notification windows, and performance benchmarks.",
    "explanation_en": "SLAs contractually define expected uptime, incident notification windows, and performance benchmarks.",
    "explanation_hi": "SLA में कानूनी रूप से लिखा होता है कि संकट आने पर कंपनी कितने मिनट में मदद करेगी और क्या सेवाएं देगी।"
  },
  {
    "id": "L3_T2_SCH_07",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "Does a managed SOC remove the organization's responsibility for security?",
    "question_en": "Does a managed SOC remove the organization's responsibility for security?",
    "question_hi": "क्या मैनेज्ड SOC किराए पर लेने से संगठन की अपनी सुरक्षा जिम्मेदारी समाप्त हो जाती है?",
    "options": [
      "Yes, completely",
      "No, the organization still has responsibilities",
      "Only during school hours",
      "Only for small files"
    ],
    "options_en": [
      "Yes, completely",
      "No, the organization still has responsibilities",
      "Only during school hours",
      "Only for small files"
    ],
    "options_hi": [
      "हाँ, पूरी तरह समाप्त हो जाती है",
      "नहीं, संगठन की अपनी आंतरिक सुरक्षा, पासवर्ड नीति और डेटा की अंतिम जिम्मेदारी बनी रहती है",
      "केवल स्कूल समय के दौरान",
      "केवल छोटी फ़ाइलों के लिए"
    ],
    "answer": "No, the organization still has responsibilities",
    "correctAnswerIndex": 1,
    "explanation": "Security accountability cannot be outsourced; organizations remain accountable for governance and internal hygiene.",
    "explanation_en": "Security accountability cannot be outsourced; organizations remain accountable for governance and internal hygiene.",
    "explanation_hi": "बाहरी कंपनी केवल मदद करती है; अपनी सुरक्षा नीतियां लागू करने और उपयोगकर्ताओं को जागरूक रखने की जिम्मेदारी संगठन की ही होती है।"
  },
  {
    "id": "L3_T2_SCH_08",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "Why is secure communication with a provider important?",
    "question_en": "Why is secure communication with a provider important?",
    "question_hi": "प्रदाता के साथ सुरक्षित संचार (Secure Communication) क्यों महत्वपूर्ण है?",
    "options": [
      "Security information must not be exposed to outsiders",
      "It makes threats disappear",
      "It removes the need for identity checks",
      "It makes all emails public"
    ],
    "options_en": [
      "Security information must not be exposed to outsiders",
      "It makes threats disappear",
      "It removes the need for identity checks",
      "It makes all emails public"
    ],
    "options_hi": [
      "सुरक्षा जानकारी और कमज़ोरियों को बाहरी लोगों के सामने उजागर नहीं होना चाहिए",
      "यह खतरों को गायब कर देता है",
      "यह पहचान जांच की आवश्यकता को समाप्त करता है",
      "यह सभी ईमेल को सार्वजनिक बनाता है"
    ],
    "answer": "Security information must not be exposed to outsiders",
    "correctAnswerIndex": 0,
    "explanation": "Encrypted communication ensures threat intelligence and vulnerability disclosures remain confidential.",
    "explanation_en": "Encrypted communication ensures threat intelligence and vulnerability disclosures remain confidential.",
    "explanation_hi": "सुरक्षा अलर्ट और नेटवर्क की कमज़ोरियों पर चर्चा केवल एन्क्रिप्टेड और सुरक्षित माध्यम से ही की जानी चाहिए।"
  },
  {
    "id": "L3_T2_SCH_09",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "Which task might a managed SOC perform?",
    "question_en": "Which task might a managed SOC perform?",
    "question_hi": "एक मैनेज्ड SOC इनमें से कौन सा कार्य कर सकता है?",
    "options": [
      "Monitor security alerts and investigate suspicious events",
      "Deliver school lunches",
      "Replace every computer screen",
      "Write student exam answers"
    ],
    "options_en": [
      "Monitor security alerts and investigate suspicious events",
      "Deliver school lunches",
      "Replace every computer screen",
      "Write student exam answers"
    ],
    "options_hi": [
      "सुरक्षा अलर्ट की निगरानी करना और संदिग्ध घटनाओं की जांच करना",
      "स्कूल का दोपहर का भोजन वितरित करना",
      "प्रत्येक कंप्यूटर स्क्रीन को बदलना",
      "छात्रों के परीक्षा उत्तर लिखना"
    ],
    "answer": "Monitor security alerts and investigate suspicious events",
    "correctAnswerIndex": 0,
    "explanation": "Core Managed SOC deliverables include SIEM monitoring, threat hunting, and preliminary incident forensics.",
    "explanation_en": "Core Managed SOC deliverables include SIEM monitoring, threat hunting, and preliminary incident forensics.",
    "explanation_hi": "मैनेज्ड SOC का काम सुरक्षा घटनाओं पर नज़र रखना और नेटवर्क में किसी असामान्य हरकत की जांच करना है।"
  },
  {
    "id": "L3_T2_SCH_10",
    "level": 3,
    "topic": "Managed SOC",
    "topicId": "managed_soc",
    "mode": "school",
    "question": "What should happen when a provider's contract ends?",
    "question_en": "What should happen when a provider's contract ends?",
    "question_hi": "जब किसी प्रदाता का अनुबंध (Contract) समाप्त होता है तो क्या किया जाना चाहिए?",
    "options": [
      "Remove unnecessary provider access and securely transfer relevant records",
      "Keep all access open forever",
      "Publish credentials",
      "Delete every security policy"
    ],
    "options_en": [
      "Remove unnecessary provider access and securely transfer relevant records",
      "Keep all access open forever",
      "Publish credentials",
      "Delete every security policy"
    ],
    "options_hi": [
      "प्रदाता की सभी सिस्टम पहुँच (Access) रद्द करें और सभी प्रासंगिक सुरक्षा रिकॉर्ड सुरक्षित रूप से वापस लें",
      "सभी पहुँच को हमेशा के लिए खुला रखें",
      "क्रेडेंशियल सार्वजनिक करें",
      "प्रत्येक सुरक्षा नीति को हटा दें"
    ],
    "answer": "Remove unnecessary provider access and securely transfer relevant records",
    "correctAnswerIndex": 0,
    "explanation": "Offboarding entails credential revocation, API key regeneration, and returning audit historical archives.",
    "explanation_en": "Offboarding entails credential revocation, API key regeneration, and returning audit historical archives.",
    "explanation_hi": "अनुबंध समाप्त होने पर बाहरी कंपनी के सभी लॉगिन और पासवर्ड तुरंत निरस्त कर देने चाहिए।"
  },

  # Topic 13 (L3 T3): Hybrid SOC
  {
    "id": "L3_T3_SCH_01",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "What is a hybrid SOC?",
    "question_en": "What is a hybrid SOC?",
    "question_hi": "हाइब्रिड SOC (Hybrid SOC) क्या है?",
    "options": [
      "A model combining internal SOC capabilities with external services",
      "A firewall made of two screens",
      "A SOC that never uses technology",
      "A public chat room"
    ],
    "options_en": [
      "A model combining internal SOC capabilities with external services",
      "A firewall made of two screens",
      "A SOC that never uses technology",
      "A public chat room"
    ],
    "options_hi": [
      "एक ऐसा मॉडल जो आंतरिक टीम की क्षमताओं को बाहरी विशेषज्ञ सेवाओं के साथ जोड़ता है",
      "दो स्क्रीन से बना फ़ायरवॉल",
      "एक SOC जो कभी तकनीक का उपयोग नहीं करता",
      "एक सार्वजनिक चैट रूम"
    ],
    "answer": "A model combining internal SOC capabilities with external services",
    "correctAnswerIndex": 0,
    "explanation": "Hybrid SOC pairs an in-house security staff with a managed security service provider for shared coverage.",
    "explanation_en": "Hybrid SOC pairs an in-house security staff with a managed security service provider for shared coverage.",
    "explanation_hi": "हाइब्रिड SOC में आंतरिक टीम और बाहरी विशेषज्ञ दोनों मिलकर सुरक्षा संभालते हैं।"
  },
  {
    "id": "L3_T3_SCH_02",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "Why might a company choose a hybrid SOC?",
    "question_en": "Why might a company choose a hybrid SOC?",
    "question_hi": "कोई संगठन हाइब्रिड SOC का चयन क्यों कर सकता है?",
    "options": [
      "It can combine internal knowledge with outside expertise",
      "It means no one monitors systems",
      "It makes all risks disappear",
      "It removes the need for staff"
    ],
    "options_en": [
      "It can combine internal knowledge with outside expertise",
      "It means no one monitors systems",
      "It makes all risks disappear",
      "It removes the need for staff"
    ],
    "options_hi": [
      "यह संगठन के आंतरिक ज्ञान को बाहरी विशेषज्ञों की विशेषज्ञता के साथ जोड़ सकता है",
      "इसका मतलब है कि कोई भी सिस्टम की निगरानी नहीं करता",
      "यह सभी जोखिमों को गायब कर देता है",
      "यह कर्मचारियों की आवश्यकता को समाप्त करता है"
    ],
    "answer": "It can combine internal knowledge with outside expertise",
    "correctAnswerIndex": 0,
    "explanation": "In-house staff understand business context while the external partner supplies 24/7 staffing and tooling.",
    "explanation_en": "In-house staff understand business context while the external partner supplies 24/7 staffing and tooling.",
    "explanation_hi": "आंतरिक टीम अपने स्कूल या कंपनी को अच्छी तरह समझती है, और बाहरी कंपनी चौबीसों घंटे निगरानी में मदद करती है।"
  },
  {
    "id": "L3_T3_SCH_03",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "What is important when internal and external analysts work together?",
    "question_en": "What is important when internal and external analysts work together?",
    "question_hi": "जब आंतरिक और बाहरी विश्लेषक एक साथ काम करते हैं तो क्या महत्वपूर्ण होता है?",
    "options": [
      "Clear roles, secure information sharing, and escalation steps",
      "Sharing passwords in public",
      "Keeping all alerts secret from the team",
      "Avoiding all documentation"
    ],
    "options_en": [
      "Clear roles, secure information sharing, and escalation steps",
      "Sharing passwords in public",
      "Keeping all alerts secret from the team",
      "Avoiding all documentation"
    ],
    "options_hi": [
      "स्पष्ट भूमिकाएं, सुरक्षित सूचना साझाकरण और एस्केलेशन प्रक्रियाएं",
      "सार्वजनिक रूप से पासवर्ड साझा करना",
      "टीम से सभी अलर्ट गुप्त रखना",
      "सभी दस्तावेज़ीकरण से बचना"
    ],
    "answer": "Clear roles, secure information sharing, and escalation steps",
    "correctAnswerIndex": 0,
    "explanation": "Clear responsibility matrices (RACI) avoid duplicated effort or overlooked security events.",
    "explanation_en": "Clear responsibility matrices (RACI) avoid duplicated effort or overlooked security events.",
    "explanation_hi": "दोनों टीमों के बीच स्पष्ट भूमिकाएं तय होनी चाहिए कि कौन सा काम कौन करेगा और कब सूचित करेगा।"
  },
  {
    "id": "L3_T3_SCH_04",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "Who should know which team handles a serious alert?",
    "question_en": "Who should know which team handles a serious alert?",
    "question_hi": "यह किसे पता होना चाहिए कि किसी गंभीर अलर्ट को कौन सी टीम संभालेगी?",
    "options": [
      "Both teams, according to their agreed responsibilities",
      "Only an unknown internet user",
      "Nobody",
      "Every public website"
    ],
    "options_en": [
      "Both teams, according to their agreed responsibilities",
      "Only an unknown internet user",
      "Nobody",
      "Every public website"
    ],
    "options_hi": [
      "दोनों टीमों को, उनकी पारस्परिक सहमत जिम्मेदारियों के अनुसार",
      "केवल एक अज्ञात इंटरनेट उपयोगकर्ता को",
      "किसी को नहीं",
      "प्रत्येक सार्वजनिक वेबसाइट को"
    ],
    "answer": "Both teams, according to their agreed responsibilities",
    "correctAnswerIndex": 0,
    "explanation": "Mutual clarity on workflows ensures rapid triage and remediation without jurisdictional confusion.",
    "explanation_en": "Mutual clarity on workflows ensures rapid triage and remediation without jurisdictional confusion.",
    "explanation_hi": "गंभीर स्थिति में दोनों टीमों को पहले से पता होना चाहिए कि किसे क्या कदम उठाना है।"
  },
  {
    "id": "L3_T3_SCH_05",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "Can a hybrid SOC use outside experts for specialist investigations?",
    "question_en": "Can a hybrid SOC use outside experts for specialist investigations?",
    "question_hi": "क्या एक हाइब्रिड SOC जटिल या विशेषज्ञ जांच के लिए बाहरी विशेषज्ञों की मदद ले सकता है?",
    "options": [
      "Yes",
      "No, external experts can never help",
      "Only for printing",
      "Only without permission"
    ],
    "options_en": [
      "Yes",
      "No, external experts can never help",
      "Only for printing",
      "Only without permission"
    ],
    "options_hi": [
      "हाँ, डिजिटल फॉरेंसिक और उन्नत मैलवेयर विश्लेषण के लिए बाहरी विशेषज्ञों की मदद ली जा सकती है",
      "नहीं, बाहरी विशेषज्ञ कभी मदद नहीं कर सकते",
      "केवल प्रिंटिंग के लिए",
      "केवल बिना अनुमति के"
    ],
    "answer": "Yes",
    "correctAnswerIndex": 0,
    "explanation": "Organizations leverage external retainers for advanced digital forensics and incident response (DFIR).",
    "explanation_en": "Organizations leverage external retainers for advanced digital forensics and incident response (DFIR).",
    "explanation_hi": "बड़ी घटनाओं में फॉरेंसिक जांच के लिए बाहरी विशेषज्ञों को बुलाना हाइब्रिड मॉडल का बड़ा फायदा है।"
  },
  {
    "id": "L3_T3_SCH_06",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "Why should a hybrid SOC test its response process?",
    "question_en": "Why should a hybrid SOC test its response process?",
    "question_hi": "हाइब्रिड SOC को अपनी प्रतिक्रिया प्रक्रिया (Response Process) का समय-समय पर परीक्षण क्यों करना चाहिए?",
    "options": [
      "To find communication or handoff problems before a real incident",
      "To remove all access controls",
      "To guarantee zero risk",
      "To make passwords public"
    ],
    "options_en": [
      "To find communication or handoff problems before a real incident",
      "To remove all access controls",
      "To guarantee zero risk",
      "To make passwords public"
    ],
    "options_hi": [
      "वास्तविक आपातकाल से पहले संचार या ज़िम्मेदारी सौंपने की समस्याओं की पहचान करने के लिए",
      "सभी एक्सेस नियंत्रणों को हटाने के लिए",
      "शून्य जोखिम की गारंटी के लिए",
      "पासवर्ड सार्वजनिक करने के लिए"
    ],
    "answer": "To find communication or handoff problems before a real incident",
    "correctAnswerIndex": 0,
    "explanation": "Tabletop exercises validate coordination workflows between internal and external analysts.",
    "explanation_en": "Tabletop exercises validate coordination workflows between internal and external analysts.",
    "explanation_hi": "मॉक ड्रिल करने से पता चलता है कि दोनों टीमों के बीच बातचीत में कोई रुकावट तो नहीं है।"
  },
  {
    "id": "L3_T3_SCH_07",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "What could happen if responsibilities are unclear?",
    "question_en": "What could happen if responsibilities are unclear?",
    "question_hi": "यदि जिम्मेदारियां स्पष्ट न हों तो क्या हो सकता है?",
    "options": [
      "An important alert may be delayed or missed",
      "All malware disappears",
      "The internet becomes faster",
      "Backups are created automatically"
    ],
    "options_en": [
      "An important alert may be delayed or missed",
      "All malware disappears",
      "The internet becomes faster",
      "Backups are created automatically"
    ],
    "options_hi": [
      "किसी महत्वपूर्ण अलर्ट पर कार्रवाई में देरी हो सकती है या वह छूट सकता है",
      "सभी मैलवेयर गायब हो जाते हैं",
      "इंटरनेट तेज़ हो जाता है",
      "बैकअप स्वचालित रूप से बनते हैं"
    ],
    "answer": "An important alert may be delayed or missed",
    "correctAnswerIndex": 0,
    "explanation": "Ambiguity causes alerts to sit unacknowledged, allowing threat actors time to pivot laterally.",
    "explanation_en": "Ambiguity causes alerts to sit unacknowledged, allowing threat actors time to pivot laterally.",
    "explanation_hi": "यदि यह तय न हो कि काम किसे करना है, तो एक टीम दूसरी पर निर्भर रहकर अलर्ट को अनदेखा कर सकती है।"
  },
  {
    "id": "L3_T3_SCH_08",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "How should confidential incident details be shared?",
    "question_en": "How should confidential incident details be shared?",
    "question_hi": "गोपनीय घटना विवरण कैसे साझा किए जाने चाहिए?",
    "options": [
      "Only with authorized people through approved channels",
      "On public social media",
      "With anyone who asks",
      "By posting passwords in a chat"
    ],
    "options_en": [
      "Only with authorized people through approved channels",
      "On public social media",
      "With anyone who asks",
      "By posting passwords in a chat"
    ],
    "options_hi": [
      "केवल अधिकृत व्यक्तियों के साथ स्वीकृत और एन्क्रिप्टेड चैनलों के माध्यम से",
      "सार्वजनिक सोशल मीडिया पर",
      "पूछने वाले किसी भी व्यक्ति के साथ",
      "चैट में पासवर्ड पोस्ट करके"
    ],
    "answer": "Only with authorized people through approved channels",
    "correctAnswerIndex": 0,
    "explanation": "Restricting incident intelligence prevents leaks that could alert attackers or violate privacy regulations.",
    "explanation_en": "Restricting incident intelligence prevents leaks that could alert attackers or violate privacy regulations.",
    "explanation_hi": "सुरक्षा घटना से जुड़ी जानकारी केवल उन्हीं लोगों तक सीमित रहनी चाहिए जो उससे निपटने के लिए अधिकृत हैं।"
  },
  {
    "id": "L3_T3_SCH_09",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "What can internal staff contribute to a hybrid SOC?",
    "question_en": "What can internal staff contribute to a hybrid SOC?",
    "question_hi": "आंतरिक कर्मचारी हाइब्रिड SOC में क्या योगदान दे सकते हैं?",
    "options": [
      "Knowledge of the organization's systems and priorities",
      "A guarantee that attacks cannot happen",
      "Public copies of every password",
      "No information at all"
    ],
    "options_en": [
      "Knowledge of the organization's systems and priorities",
      "A guarantee that attacks cannot happen",
      "Public copies of every password",
      "No information at all"
    ],
    "options_hi": [
      "संगठन के सिस्टम, व्यावसायिक प्राथमिकताओं और नेटवर्क के आंतरिक कामकाज का गहन ज्ञान",
      "यह गारंटी कि हमले नहीं हो सकते",
      "प्रत्येक पासवर्ड की सार्वजनिक प्रतियां",
      "कोई जानकारी नहीं"
    ],
    "answer": "Knowledge of the organization's systems and priorities",
    "correctAnswerIndex": 0,
    "explanation": "Internal teams provide critical context on asset criticality, normal business baselines, and users.",
    "explanation_en": "Internal teams provide critical context on asset criticality, normal business baselines, and users.",
    "explanation_hi": "आंतरिक कर्मचारी जानते हैं कि कौन सा सर्वर और डेटा सबसे महत्वपूर्ण है, जिससे सही निर्णय लिए जा सकते हैं।"
  },
  {
    "id": "L3_T3_SCH_10",
    "level": 3,
    "topic": "Hybrid SOC",
    "topicId": "hybrid_soc",
    "mode": "school",
    "question": "What is a useful outcome after a hybrid SOC incident?",
    "question_en": "What is a useful outcome after a hybrid SOC incident?",
    "question_hi": "हाइब्रिड SOC सुरक्षा घटना के बाद एक उपयोगी परिणाम क्या होना चाहिए?",
    "options": [
      "Review the teamwork and improve the process",
      "Blame others without checking facts",
      "Erase logs immediately",
      "Stop monitoring permanently"
    ],
    "options_en": [
      "Review the teamwork and improve the process",
      "Blame others without checking facts",
      "Erase logs immediately",
      "Stop monitoring permanently"
    ],
    "options_hi": [
      "दोनों टीमों के समन्वय की समीक्षा करना और सुरक्षा प्रक्रिया में सुधार करना",
      "तथ्यों की जांच किए बिना दूसरों पर दोषारोपण करना",
      "लॉग्स को तुरंत मिटा देना",
      "स्थायी रूप से निगरानी बंद करना"
    ],
    "answer": "Review the teamwork and improve the process",
    "correctAnswerIndex": 0,
    "explanation": "Collaborative post-mortems refine playbook triggers and strengthen cross-organizational teamwork.",
    "explanation_en": "Collaborative post-mortems refine playbook triggers and strengthen cross-organizational teamwork.",
    "explanation_hi": "घटना के बाद दोनों टीमों को मिलकर यह देखना चाहिए कि भविष्य में समन्वय को और कैसे बेहतर बनाया जाए।"
  },

  # Topic 14 (L3 T4): Co-Managed SOC
  {
    "id": "L3_T4_SCH_01",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "What is a co-managed SOC?",
    "question_en": "What is a co-managed SOC?",
    "question_hi": "को-मैनेज्ड SOC (Co-Managed SOC) क्या है?",
    "options": [
      "An internal security team and an outside provider share SOC responsibilities",
      "A SOC with no people",
      "A public Wi-Fi service",
      "A password-sharing group"
    ],
    "options_en": [
      "An internal security team and an outside provider share SOC responsibilities",
      "A SOC with no people",
      "A public Wi-Fi service",
      "A password-sharing group"
    ],
    "options_hi": [
      "एक ऐसा मॉडल जिसमें आंतरिक सुरक्षा टीम और बाहरी सेवा प्रदाता SOC जिम्मेदारियों को साझा करते हैं",
      "बिना लोगों वाला एक SOC",
      "एक सार्वजनिक वाई-फ़ाई सेवा",
      "एक पासवर्ड-शेयरिंग समूह"
    ],
    "answer": "An internal security team and an outside provider share SOC responsibilities",
    "correctAnswerIndex": 0,
    "explanation": "Co-management features shared administrative controls, toolsets, and joint operational accountability.",
    "explanation_en": "Co-management features shared administrative controls, toolsets, and joint operational accountability.",
    "explanation_hi": "को-मैनेज्ड SOC में आंतरिक और बाहरी टीमें एक ही सिस्टम और टूल्स पर मिलकर समान रूप से काम करती हैं।"
  },
  {
    "id": "L3_T4_SCH_02",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "In a co-managed SOC, why should duties be clearly divided?",
    "question_en": "In a co-managed SOC, why should duties be clearly divided?",
    "question_hi": "को-मैनेज्ड SOC में कर्तव्यों का स्पष्ट विभाजन क्यों होना चाहिए?",
    "options": [
      "So each alert and task has an accountable owner",
      "So every task is ignored",
      "So passwords can be shared freely",
      "So logs need not be reviewed"
    ],
    "options_en": [
      "So each alert and task has an accountable owner",
      "So every task is ignored",
      "So passwords can be shared freely",
      "So logs need not be reviewed"
    ],
    "options_hi": [
      "ताकि प्रत्येक अलर्ट और सुरक्षा कार्य का एक स्पष्ट उत्तरदायी व्यक्ति (Owner) हो",
      "ताकि हर कार्य की उपेक्षा की जा सके",
      "ताकि पासवर्ड स्वतंत्र रूप से साझा किए जा सकें",
      "ताकि लॉग्स की समीक्षा करने की आवश्यकता न हो"
    ],
    "answer": "So each alert and task has an accountable owner",
    "correctAnswerIndex": 0,
    "explanation": "Clearly defined duties prevent coverage gaps during threat analysis and incident escalation.",
    "explanation_en": "Clearly defined duties prevent coverage gaps during threat analysis and incident escalation.",
    "explanation_hi": "स्पष्ट जिम्मेदारी तय होने से यह सुनिश्चित होता है कि हर खतरे पर तुरंत और सही तरीके से काम किया जा रहा है।"
  },
  {
    "id": "L3_T4_SCH_03",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "What might an outside provider contribute to a co-managed SOC?",
    "question_en": "What might an outside provider contribute to a co-managed SOC?",
    "question_hi": "एक बाहरी सेवा प्रदाता को-मैनेज्ड SOC में क्या योगदान दे सकता है?",
    "options": [
      "Extra monitoring expertise or specialist tools",
      "Guaranteed protection from all attacks",
      "Access to every private account",
      "A replacement for all company policies"
    ],
    "options_en": [
      "Extra monitoring expertise or specialist tools",
      "Guaranteed protection from all attacks",
      "Access to every private account",
      "A replacement for all company policies"
    ],
    "options_hi": [
      "अतिरिक्त निगरानी विशेषज्ञता या उन्नत सुरक्षा उपकरण (Tools)",
      "सभी हमलों से गारंटीकृत सुरक्षा",
      "प्रत्येक निजी खाते तक पहुँच",
      "कंपनी की सभी नीतियों का प्रतिस्थापन"
    ],
    "answer": "Extra monitoring expertise or specialist tools",
    "correctAnswerIndex": 0,
    "explanation": "External partners bring specialized SIEM, SOAR platforms, and threat intelligence feeds.",
    "explanation_en": "External partners bring specialized SIEM, SOAR platforms, and threat intelligence feeds.",
    "explanation_hi": "बाहरी कंपनी आधुनिक निगरानी उपकरण और अनुभवी सुरक्षा विश्लेषक उपलब्ध कराती है।"
  },
  {
    "id": "L3_T4_SCH_04",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "Why should internal staff still receive security training?",
    "question_en": "Why should internal staff still receive security training?",
    "question_hi": "आंतरिक कर्मचारियों को अभी भी सुरक्षा प्रशिक्षण क्यों प्राप्त करना चाहिए?",
    "options": [
      "They remain part of the security process and need to respond correctly",
      "Training makes incidents impossible",
      "Only external teams use computers",
      "It removes the need for updates"
    ],
    "options_en": [
      "They remain part of the security process and need to respond correctly",
      "Training makes incidents impossible",
      "Only external teams use computers",
      "It removes the need for updates"
    ],
    "options_hi": [
      "वे सुरक्षा प्रक्रिया का अभिन्न हिस्सा हैं और उन्हें सही प्रतिक्रिया देने की आवश्यकता होती है",
      "प्रशिक्षण घटनाओं को असंभव बना देता है",
      "केवल बाहरी टीमें कंप्यूटर का उपयोग करती हैं",
      "यह अपडेट की आवश्यकता को समाप्त करता है"
    ],
    "answer": "They remain part of the security process and need to respond correctly",
    "correctAnswerIndex": 0,
    "explanation": "Human awareness remains the primary defense line against social engineering and credential compromise.",
    "explanation_en": "Human awareness remains the primary defense line against social engineering and credential compromise.",
    "explanation_hi": "कर्मचारी ही सिस्टम का उपयोग करते हैं; यदि वे प्रशिक्षित नहीं होंगे तो फ़िशिंग या मैलवेयर का शिकार हो सकते हैं।"
  },
  {
    "id": "L3_T4_SCH_05",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "What should be agreed before a provider begins co-managed work?",
    "question_en": "What should be agreed before a provider begins co-managed work?",
    "question_hi": "प्रदाता द्वारा सह-प्रबंधित (Co-managed) कार्य शुरू करने से पहले क्या सहमति बननी चाहिए?",
    "options": [
      "Access permissions, responsibilities, and escalation procedures",
      "The public release of passwords",
      "That alerts will never be reported",
      "That backups will be deleted"
    ],
    "options_en": [
      "Access permissions, responsibilities, and escalation procedures",
      "The public release of passwords",
      "That alerts will never be reported",
      "That backups will be deleted"
    ],
    "options_hi": [
      "पहुँच अनुमतियाँ (Permissions), जिम्मेदारियाँ और एस्केलेशन प्रक्रियाएं",
      "पासवर्ड जारी करना",
      "कि अलर्ट कभी रिपोर्ट नहीं किए जाएंगे",
      "कि बैकअप हटा दिए जाएंगे"
    ],
    "answer": "Access permissions, responsibilities, and escalation procedures",
    "correctAnswerIndex": 0,
    "explanation": "Establishing access boundaries and escalation thresholds upfront ensures disciplined incident coordination.",
    "explanation_en": "Establishing access boundaries and escalation thresholds upfront ensures disciplined incident coordination.",
    "explanation_hi": "काम शुरू होने से पहले अनुबंध में यह स्पष्ट होना चाहिए कि किसे कौन सी पहुंच मिलेगी और संकट में क्या करना होगा।"
  },
  {
    "id": "L3_T4_SCH_06",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "If an incident occurs, why is a shared response plan useful?",
    "question_en": "If an incident occurs, why is a shared response plan useful?",
    "question_hi": "यदि कोई सुरक्षा घटना घटती है, तो एक साझा प्रतिक्रिया योजना (Shared Response Plan) क्यों उपयोगी होती है?",
    "options": [
      "It helps both teams act in a coordinated way",
      "It guarantees no damage",
      "It makes evidence unnecessary",
      "It stops all communication"
    ],
    "options_en": [
      "It helps both teams act in a coordinated way",
      "It guarantees no damage",
      "It makes evidence unnecessary",
      "It stops all communication"
    ],
    "options_hi": [
      "यह दोनों टीमों को समन्वित और प्रभावी तरीके से कार्य करने में मदद करती है",
      "यह किसी नुकसान न होने की गारंटी देती है",
      "यह साक्ष्य को अनावश्यक बनाती है",
      "यह सभी संचार रोक देती है"
    ],
    "answer": "It helps both teams act in a coordinated way",
    "correctAnswerIndex": 0,
    "explanation": "A synchronized playbook ensures containment actions occur swiftly without conflicting steps.",
    "explanation_en": "A synchronized playbook ensures containment actions occur swiftly without conflicting steps.",
    "explanation_hi": "साझा योजना होने से दोनों टीमों को पहले से पता होता है कि किसे क्या कदम उठाना है, जिससे समय बचता है।"
  },
  {
    "id": "L3_T4_SCH_07",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "Which is a sensible access rule for an outside provider?",
    "question_en": "Which is a sensible access rule for an outside provider?",
    "question_hi": "किसी बाहरी प्रदाता के लिए कौन सा एक समझदारी भरा एक्सेस नियम है?",
    "options": [
      "Grant only the permissions required for the agreed tasks",
      "Give permanent administrator access to everyone",
      "Share one account with all staff",
      "Disable authentication"
    ],
    "options_en": [
      "Grant only the permissions required for the agreed tasks",
      "Give permanent administrator access to everyone",
      "Share one account with all staff",
      "Disable authentication"
    ],
    "options_hi": [
      "केवल तय किए गए कार्यों के लिए आवश्यक अनुमतियाँ ही प्रदान करें (कम से कम विशेषाधिकार)",
      "सभी को स्थायी व्यवस्थापक (Admin) एक्सेस दें",
      "सभी कर्मचारियों के साथ एक ही खाता साझा करें",
      "प्रमाणीकरण अक्षम करें"
    ],
    "answer": "Grant only the permissions required for the agreed tasks",
    "correctAnswerIndex": 0,
    "explanation": "Role-based access control enforces least privilege for external collaborators.",
    "explanation_en": "Role-based access control enforces least privilege for external collaborators.",
    "explanation_hi": "बाहरी कंपनी के इंजीनियरों को केवल वही अधिकार दें जो उनके काम के लिए ज़रूरी हैं, पूरा एडमिन अधिकार नहीं।"
  },
  {
    "id": "L3_T4_SCH_08",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "How can a co-managed SOC improve over time?",
    "question_en": "How can a co-managed SOC improve over time?",
    "question_hi": "एक को-मैनेज्ड SOC समय के साथ अपने प्रदर्शन में कैसे सुधार कर सकता है?",
    "options": [
      "Review incidents, measure performance, and update procedures",
      "Ignore repeated issues",
      "Remove monitoring tools",
      "Publish security logs publicly"
    ],
    "options_en": [
      "Review incidents, measure performance, and update procedures",
      "Ignore repeated issues",
      "Remove monitoring tools",
      "Publish security logs publicly"
    ],
    "options_hi": [
      "घटनाओं की समीक्षा करें, प्रदर्शन को मापें और प्रक्रियाओं को नियमित रूप से अपडेट करें",
      "बार-बार होने वाली समस्याओं को अनदेखा करें",
      "निगरानी उपकरण हटा दें",
      "सुरक्षा लॉग सार्वजनिक रूप से प्रकाशित करें"
    ],
    "answer": "Review incidents, measure performance, and update procedures",
    "correctAnswerIndex": 0,
    "explanation": "Continuous improvement relies on metrics like MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond).",
    "explanation_en": "Continuous improvement relies on metrics like MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond).",
    "explanation_hi": "पुरानी घटनाओं से सीखकर और प्रतिक्रिया समय को मापकर सुरक्षा प्रणाली को लगातार मजबूत किया जाता है।"
  },
  {
    "id": "L3_T4_SCH_09",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "What should happen if the provider no longer needs access?",
    "question_en": "What should happen if the provider no longer needs access?",
    "question_hi": "यदि प्रदाता को अब सिस्टम एक्सेस की आवश्यकता नहीं है, तो क्या किया जाना चाहिए?",
    "options": [
      "Revoke or reduce that access",
      "Leave it active forever",
      "Share it with students",
      "Write it on a poster"
    ],
    "options_en": [
      "Revoke or reduce that access",
      "Leave it active forever",
      "Share it with students",
      "Write it on a poster"
    ],
    "options_hi": [
      "उस एक्सेस को तुरंत निरस्त (Revoke) या कम कर दिया जाना चाहिए",
      "इसे हमेशा के लिए सक्रिय छोड़ दें",
      "इसे छात्रों के साथ साझा करें",
      "इसे पोस्टर पर लिखें"
    ],
    "answer": "Revoke or reduce that access",
    "correctAnswerIndex": 0,
    "explanation": "Dormant administrative accounts are high-value targets for attackers and must be decommissioned immediately.",
    "explanation_en": "Dormant administrative accounts are high-value targets for attackers and must be decommissioned immediately.",
    "explanation_hi": "आवश्यकता समाप्त होते ही बाहरी खातों को बंद कर देना चाहिए ताकि वे सुरक्षा में कमज़ोरी न बनें।"
  },
  {
    "id": "L3_T4_SCH_10",
    "level": 3,
    "topic": "Co-Managed SOC",
    "topicId": "comanaged_soc",
    "mode": "school",
    "question": "What is a key benefit of co-management?",
    "question_en": "What is a key benefit of co-management?",
    "question_hi": "सह-प्रबंधन (Co-management) का एक प्रमुख लाभ क्या है?",
    "options": [
      "The organization can combine its own knowledge with specialist support",
      "The organization no longer has any responsibilities",
      "All threats become harmless",
      "No security staff are needed"
    ],
    "options_en": [
      "The organization can combine its own knowledge with specialist support",
      "The organization no longer has any responsibilities",
      "All threats become harmless",
      "No security staff are needed"
    ],
    "options_hi": [
      "संगठन अपने आंतरिक ज्ञान को बाहरी विशेषज्ञों के समर्थन के साथ जोड़ सकता है",
      "संगठन की कोई जिम्मेदारी नहीं रह जाती",
      "सभी खतरे हानिरहित हो जाते हैं",
      "किसी सुरक्षा कर्मचारी की आवश्यकता नहीं है"
    ],
    "answer": "The organization can combine its own knowledge with specialist support",
    "correctAnswerIndex": 0,
    "explanation": "Co-management preserves institutional knowledge while gaining external specialized capabilities.",
    "explanation_en": "Co-management preserves institutional knowledge while gaining external specialized capabilities.",
    "explanation_hi": "संगठन अपनी स्वायत्तता बनाए रखते हुए बाहरी विशेषज्ञों की विशेषज्ञता का पूरा फायदा उठा सकता है।"
  },

  # Topic 15 (L3 T5): Virtual SOC (vSOC)
  {
    "id": "L3_T5_SCH_01",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "What is a virtual SOC?",
    "question_en": "What is a virtual SOC?",
    "question_hi": "वर्चुअल SOC (vSOC - Virtual SOC) क्या है?",
    "options": [
      "A security operations team that works remotely using digital tools",
      "A fictional team in a video game",
      "A computer with no network",
      "A printed security poster"
    ],
    "options_en": [
      "A security operations team that works remotely using digital tools",
      "A fictional team in a video game",
      "A computer with no network",
      "A printed security poster"
    ],
    "options_hi": [
      "एक सुरक्षा संचालन टीम जो डिजिटल टूल्स और क्लाउड के ज़रिए दूरस्थ (Remotely) रूप से काम करती है",
      "एक वीडियो गेम में एक काल्पनिक टीम",
      "बिना नेटवर्क वाला कंप्यूटर",
      "एक मुद्रित सुरक्षा पोस्टर"
    ],
    "answer": "A security operations team that works remotely using digital tools",
    "correctAnswerIndex": 0,
    "explanation": "A vSOC utilizes cloud SIEM and collaborative platforms to deliver security monitoring without a physical facility.",
    "explanation_en": "A vSOC utilizes cloud SIEM and collaborative platforms to deliver security monitoring without a physical facility.",
    "explanation_hi": "वर्चुअल SOC किसी एक भौतिक कमरे में बैठने के बजाय क्लाउड टूल्स की मदद से रिमोट काम करता है।"
  },
  {
    "id": "L3_T5_SCH_02",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "What does a virtual SOC need to access systems safely?",
    "question_en": "What does a virtual SOC need to access systems safely?",
    "question_hi": "एक वर्चुअल SOC को सिस्टम तक सुरक्षित रूप से पहुँचने के लिए किसकी आवश्यकता होती है?",
    "options": [
      "Approved secure connections and strong authentication",
      "Public passwords",
      "Unknown remote-access apps",
      "No access controls"
    ],
    "options_en": [
      "Approved secure connections and strong authentication",
      "Public passwords",
      "Unknown remote-access apps",
      "No access controls"
    ],
    "options_hi": [
      "स्वीकृत सुरक्षित कनेक्शन (जैसे VPN/ZTNA) और मजबूत प्रमाणीकरण (MFA)",
      "सार्वजनिक पासवर्ड",
      "अज्ञात रिमोट-एक्सेस ऐप्स",
      "कोई एक्सेस नियंत्रण नहीं"
    ],
    "answer": "Approved secure connections and strong authentication",
    "correctAnswerIndex": 0,
    "explanation": "Secure tunnels (VPN/ZTNA) and hardware-backed multi-factor authentication protect analyst access.",
    "explanation_en": "Secure tunnels (VPN/ZTNA) and hardware-backed multi-factor authentication protect analyst access.",
    "explanation_hi": "दूर बैठकर काम करने वाले सुरक्षा विश्लेषकों को एन्क्रिप्टेड VPN और टू-फ़ैक्टर ऑथेंटिकेशन का उपयोग करना होता है।"
  },
  {
    "id": "L3_T5_SCH_03",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "Why are dashboards useful to a virtual SOC?",
    "question_en": "Why are dashboards useful to a virtual SOC?",
    "question_hi": "डैशबोर्ड (Dashboards) वर्चुअल SOC के लिए क्यों उपयोगी हैं?",
    "options": [
      "They help analysts view alerts and system status remotely",
      "They automatically stop every attack",
      "They replace all investigation",
      "They publish passwords"
    ],
    "options_en": [
      "They help analysts view alerts and system status remotely",
      "They automatically stop every attack",
      "They replace all investigation",
      "They publish passwords"
    ],
    "options_hi": [
      "वे विश्लेषकों को दूर से ही वास्तविक समय के अलर्ट और सिस्टम की स्थिति देखने में मदद करते हैं",
      "वे स्वचालित रूप से हर हमले को रोकते हैं",
      "वे सभी जांच की जगह लेते हैं",
      "वे पासवर्ड प्रकाशित करते हैं"
    ],
    "answer": "They help analysts view alerts and system status remotely",
    "correctAnswerIndex": 0,
    "explanation": "Dashboards visualize threat feeds, open tickets, and anomalous telemetry in a unified web console.",
    "explanation_en": "Dashboards visualize threat feeds, open tickets, and anomalous telemetry in a unified web console.",
    "explanation_hi": "डैशबोर्ड सभी नेटवर्क चेतावनियों और सुरक्षा डेटा को एक ही स्क्रीन पर साफ़-साफ़ दिखाते हैं।"
  },
  {
    "id": "L3_T5_SCH_04",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "What is a risk of poorly secured remote access?",
    "question_en": "What is a risk of poorly secured remote access?",
    "question_hi": "खराब तरीके से सुरक्षित किए गए रिमोट एक्सेस का क्या जोखिम है?",
    "options": [
      "An attacker may gain access to systems or monitoring tools",
      "The screen becomes brighter",
      "A backup becomes larger",
      "The keyboard language changes"
    ],
    "options_en": [
      "An attacker may gain access to systems or monitoring tools",
      "The screen becomes brighter",
      "A backup becomes larger",
      "The keyboard language changes"
    ],
    "options_hi": [
      "हमलावर सिस्टम या सुरक्षा निगरानी उपकरणों तक अनधिकृत पहुँच प्राप्त कर सकता है",
      "स्क्रीन अधिक चमकदार हो जाती है",
      "बैकअप बड़ा हो जाता है",
      "कीबोर्ड की भाषा बदल जाती है"
    ],
    "answer": "An attacker may gain access to systems or monitoring tools",
    "correctAnswerIndex": 0,
    "explanation": "Compromised remote access credentials give adversaries a direct entry point into core enterprise networks.",
    "explanation_en": "Compromised remote access credentials give adversaries a direct entry point into core enterprise networks.",
    "explanation_hi": "यदि रिमोट एक्सेस कमजोर हो तो हैकर सुरक्षा विश्लेषक बनकर पूरे नेटवर्क में सेंध लगा सकते हैं।"
  },
  {
    "id": "L3_T5_SCH_05",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "How can remote SOC analysts protect sensitive information?",
    "question_en": "How can remote SOC analysts protect sensitive information?",
    "question_hi": "रिमोट SOC विश्लेषक संवेदनशील जानकारी की सुरक्षा कैसे कर सकते हैं?",
    "options": [
      "Use approved devices, secure connections, and access controls",
      "Work on any public computer without logging out",
      "Send logs to personal public accounts",
      "Share credentials with friends"
    ],
    "options_en": [
      "Use approved devices, secure connections, and access controls",
      "Work on any public computer without logging out",
      "Send logs to personal public accounts",
      "Share credentials with friends"
    ],
    "options_hi": [
      "केवल स्वीकृत सुरक्षित डिवाइस, एन्क्रिप्टेड कनेक्शन और सख्त एक्सेस नियंत्रणों का उपयोग करें",
      "बिना लॉग आउट किए किसी भी सार्वजनिक कंप्यूटर पर काम करें",
      "निजी सार्वजनिक खातों में लॉग भेजें",
      "दोस्तों के साथ क्रेडेंशियल साझा करें"
    ],
    "answer": "Use approved devices, secure connections, and access controls",
    "correctAnswerIndex": 0,
    "explanation": "Hardened corporate endpoints with disk encryption and VPN enforce zero trust for remote staff.",
    "explanation_en": "Hardened corporate endpoints with disk encryption and VPN enforce zero trust for remote staff.",
    "explanation_hi": "विश्लेषकों को कंपनी द्वारा दिए गए सुरक्षित लैपटॉप और वीपीएन से ही काम करना चाहिए।"
  },
  {
    "id": "L3_T5_SCH_06",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "Can a virtual SOC support systems in different locations?",
    "question_en": "Can a virtual SOC support systems in different locations?",
    "question_hi": "क्या एक वर्चुअल SOC विभिन्न भौगोलिक स्थानों पर स्थित सिस्टमों की निगरानी कर सकता है?",
    "options": [
      "Yes",
      "No, it must be in one physical room",
      "Only without internet",
      "Only during a classroom lesson"
    ],
    "options_en": [
      "Yes",
      "No, it must be in one physical room",
      "Only without internet",
      "Only during a classroom lesson"
    ],
    "options_hi": [
      "हाँ, यह दुनिया भर में फैले कई परिसरों और क्लाउड सिस्टम की निगरानी कर सकता है",
      "नहीं, इसे एक भौतिक कमरे में होना चाहिए",
      "केवल इंटरनेट के बिना",
      "केवल कक्षा पाठ के दौरान"
    ],
    "answer": "Yes",
    "correctAnswerIndex": 0,
    "explanation": "Centralized cloud telemetry enables analysts to monitor branch offices and multi-cloud footprints globally.",
    "explanation_en": "Centralized cloud telemetry enables analysts to monitor branch offices and multi-cloud footprints globally.",
    "explanation_hi": "क्लाउड आधारित होने के कारण वर्चुअल SOC कई शहरों या देशों में फैले कार्यालयों की एक साथ निगरानी कर सकता है।"
  },
  {
    "id": "L3_T5_SCH_07",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "Why should virtual SOC accounts use multi-factor authentication?",
    "question_en": "Why should virtual SOC accounts use multi-factor authentication?",
    "question_hi": "वर्चुअल SOC खातों को मल्टी-फ़ैक्टर ऑथेंटिकेशन (MFA) का उपयोग क्यों करना चाहिए?",
    "options": [
      "It adds another check beyond a password",
      "It makes passwords public",
      "It removes the need for updates",
      "It blocks every email"
    ],
    "options_en": [
      "It adds another check beyond a password",
      "It makes passwords public",
      "It removes the need for updates",
      "It blocks every email"
    ],
    "options_hi": [
      "यह पासवर्ड के अलावा सुरक्षा का एक अतिरिक्त सत्यापन स्तर जोड़ता है",
      "यह पासवर्ड को सार्वजनिक करता है",
      "यह अपडेट की आवश्यकता को समाप्त करता है",
      "यह हर ईमेल को ब्लॉक करता है"
    ],
    "answer": "It adds another check beyond a password",
    "correctAnswerIndex": 0,
    "explanation": "MFA ensures that even if an analyst's password is leaked, unauthorized logins remain blocked.",
    "explanation_en": "MFA ensures that even if an analyst's password is leaked, unauthorized logins remain blocked.",
    "explanation_hi": "सुरक्षा नियंत्रण खातों में MFA होने से पासवर्ड लीक होने पर भी कोई अनधिकृत व्यक्ति लॉगिन नहीं कर सकता।"
  },
  {
    "id": "L3_T5_SCH_08",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "What should a remote analyst do if a monitoring connection fails?",
    "question_en": "What should a remote analyst do if a monitoring connection fails?",
    "question_hi": "यदि किसी रिमोट विश्लेषक का निगरानी कनेक्शन अचानक टूट जाता है, तो उसे क्या करना चाहिए?",
    "options": [
      "Report it and follow the approved backup or escalation procedure",
      "Ignore the outage",
      "Disable all protections",
      "Post credentials online"
    ],
    "options_en": [
      "Report it and follow the approved backup or escalation procedure",
      "Ignore the outage",
      "Disable all protections",
      "Post credentials online"
    ],
    "options_hi": [
      "तुरंत इसकी सूचना दें और स्वीकृत बैकअप या एस्केलेशन प्रक्रिया का पालन करें",
      "रुकावट को अनदेखा करें",
      "सभी सुरक्षा बंद करें",
      "क्रेडेंशियल ऑनलाइन पोस्ट करें"
    ],
    "answer": "Report it and follow the approved backup or escalation procedure",
    "correctAnswerIndex": 0,
    "explanation": "Outages in security feeds must be reported immediately to failover to backup monitoring nodes.",
    "explanation_en": "Outages in security feeds must be reported immediately to failover to backup monitoring nodes.",
    "explanation_hi": "निगरानी टूटने से सुरक्षा में अंधा क्षेत्र (Blind spot) बन जाता है, इसलिए तुरंत बैकअप प्रक्रिया शुरू करनी चाहिए।"
  },
  {
    "id": "L3_T5_SCH_09",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "Why should remote sessions be logged where appropriate?",
    "question_en": "Why should remote sessions be logged where appropriate?",
    "question_hi": "रिमोट सत्रों (Remote Sessions) को उचित रूप से क्यों लॉग किया जाना चाहिए?",
    "options": [
      "To support accountability and investigation",
      "To make users' passwords visible",
      "To replace all security tools",
      "To slow every computer"
    ],
    "options_en": [
      "To support accountability and investigation",
      "To make users' passwords visible",
      "To replace all security tools",
      "To slow every computer"
    ],
    "options_hi": [
      "जवाबदेही सुनिश्चित करने और भविष्य की जांच में सहायता के लिए",
      "उपयोगकर्ताओं के पासवर्ड को दृश्यमान बनाने के लिए",
      "सभी सुरक्षा उपकरणों को बदलने के लिए",
      "हर कंप्यूटर को धीमा करने के लिए"
    ],
    "answer": "To support accountability and investigation",
    "correctAnswerIndex": 0,
    "explanation": "Session auditing verifies that remote administrative privileges are exercised responsibly.",
    "explanation_en": "Session auditing verifies that remote administrative privileges are exercised responsibly.",
    "explanation_hi": "सत्र रिकॉर्डिंग से यह साबित होता है कि किसने कब कौन सी कार्रवाई की, जिससे जवाबदेही बनी रहती है।"
  },
  {
    "id": "L3_T5_SCH_10",
    "level": 3,
    "topic": "Virtual SOC (vSOC)",
    "topicId": "virtual_soc",
    "mode": "school",
    "question": "What is the main goal of a virtual SOC?",
    "question_en": "What is the main goal of a virtual SOC?",
    "question_hi": "वर्चुअल SOC का मुख्य लक्ष्य क्या है?",
    "options": [
      "Monitor and help protect systems remotely",
      "Provide entertainment only",
      "Replace all computer networks",
      "Make all systems public"
    ],
    "options_en": [
      "Monitor and help protect systems remotely",
      "Provide entertainment only",
      "Replace all computer networks",
      "Make all systems public"
    ],
    "options_hi": [
      "दूरस्थ रूप से सिस्टम की निरंतर निगरानी करना और खतरों से सुरक्षा प्रदान करना",
      "केवल मनोरंजन प्रदान करना",
      "सभी कंप्यूटर नेटवर्क को बदलना",
      "सभी सिस्टम को सार्वजनिक करना"
    ],
    "answer": "Monitor and help protect systems remotely",
    "correctAnswerIndex": 0,
    "explanation": "A virtual SOC delivers full threat detection, response, and resilience capabilities remotely.",
    "explanation_en": "A virtual SOC delivers full threat detection, response, and resilience capabilities remotely.",
    "explanation_hi": "वर्चुअल SOC का प्राथमिक लक्ष्य बिना भौतिक उपस्थिति के दूर से ही संपूर्ण नेटवर्क को साइबर हमलों से सुरक्षित रखना है।"
  }
]

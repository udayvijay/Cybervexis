# -*- coding: utf-8 -*-
"""Level 4: Security Architecture (5 topics x 10 questions = 50 questions)"""

level4_questions = [
  # Topic 16 (L4 T1): Identity-Based Architecture
  {
    "id": "L4_T1_SCH_01",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "What is authentication?",
    "question_en": "What is authentication?",
    "question_hi": "प्रमाणीकरण (Authentication) क्या है?",
    "options": [
      "Checking that a user or device is who it claims to be",
      "Deciding the colour of a screen",
      "Making a backup copy",
      "Connecting a printer cable"
    ],
    "options_en": [
      "Checking that a user or device is who it claims to be",
      "Deciding the colour of a screen",
      "Making a backup copy",
      "Connecting a printer cable"
    ],
    "options_hi": [
      "यह पुष्टि करना कि कोई उपयोगकर्ता या डिवाइस वास्तव में वही है जो वह होने का दावा करता है",
      "स्क्रीन का रंग तय करना",
      "बैकअप कॉपी बनाना",
      "प्रिंटर केबल कनेक्ट करना"
    ],
    "answer": "Checking that a user or device is who it claims to be",
    "correctAnswerIndex": 0,
    "explanation": "Authentication validates identity credentials (such as passwords, tokens, or biometrics).",
    "explanation_en": "Authentication validates identity credentials (such as passwords, tokens, or biometrics).",
    "explanation_hi": "प्रमाणीकरण (Authentication) यह जांचता है कि लॉगिन करने वाला व्यक्ति असली उपयोगकर्ता है या नहीं (जैसे पासवर्ड या फिंगरप्रिंट द्वारा)।"
  },
  {
    "id": "L4_T1_SCH_02",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "What is authorization?",
    "question_en": "What is authorization?",
    "question_hi": "प्राधिकरण (Authorization) क्या है?",
    "options": [
      "Deciding what an authenticated user is allowed to access",
      "Checking the weather",
      "Creating a screen saver",
      "Changing a keyboard"
    ],
    "options_en": [
      "Deciding what an authenticated user is allowed to access",
      "Checking the weather",
      "Creating a screen saver",
      "Changing a keyboard"
    ],
    "options_hi": [
      "यह तय करना कि एक प्रमाणित उपयोगकर्ता को किन संसाधनों या फ़ाइलों तक पहुँचने की अनुमति है",
      "मौसम की जांच करना",
      "स्क्रीन सेवर बनाना",
      "कीबोर्ड बदलना"
    ],
    "answer": "Deciding what an authenticated user is allowed to access",
    "correctAnswerIndex": 0,
    "explanation": "Authorization determines the permissions and access privileges granted to a verified identity.",
    "explanation_en": "Authorization determines the permissions and access privileges granted to a verified identity.",
    "explanation_hi": "प्राधिकरण (Authorization) यह निर्धारित करता है कि लॉगिन के बाद आप कौन सी फ़ाइलें देख सकते हैं या बदल सकते हैं।"
  },
  {
    "id": "L4_T1_SCH_03",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "A student needs to view homework but not edit school records. Which principle applies?",
    "question_en": "A student needs to view homework but not edit school records. Which principle applies?",
    "question_hi": "एक छात्र को गृहकार्य देखना है लेकिन स्कूल के आधिकारिक रिकॉर्ड बदलने की अनुमति नहीं होनी चाहिए। यहाँ कौन सा सिद्धांत लागू होता है?",
    "options": [
      "Least privilege",
      "Public access",
      "Password reuse",
      "Open sharing"
    ],
    "options_en": [
      "Least privilege",
      "Public access",
      "Password reuse",
      "Open sharing"
    ],
    "options_hi": [
      "न्यूनतम विशेषाधिकार (Least Privilege)",
      "सार्वजनिक पहुँच",
      "पासवर्ड का पुन: उपयोग",
      "खुला साझाकरण"
    ],
    "answer": "Least privilege",
    "correctAnswerIndex": 0,
    "explanation": "Least privilege grants only the minimal permissions necessary to perform required tasks.",
    "explanation_en": "Least privilege grants only the minimal permissions necessary to perform required tasks.",
    "explanation_hi": "न्यूनतम विशेषाधिकार का सिद्धांत कहता है कि उपयोगकर्ता को केवल वही अनुमति दी जाए जिसकी उसके काम के लिए आवश्यकता हो।"
  },
  {
    "id": "L4_T1_SCH_04",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "Why should each student have an individual account?",
    "question_en": "Why should each student have an individual account?",
    "question_hi": "प्रत्येक छात्र का अपना अलग व्यक्तिगत खाता क्यों होना चाहिए?",
    "options": [
      "Actions can be linked to the correct account and access can be controlled",
      "Everyone can share one password",
      "It removes the need for security",
      "It makes all records public"
    ],
    "options_en": [
      "Actions can be linked to the correct account and access can be controlled",
      "Everyone can share one password",
      "It removes the need for security",
      "It makes all records public"
    ],
    "options_hi": [
      "कार्रवाइयों को सही खाते से जोड़ा जा सकता है (जवाबदेही) और पहुँच को नियंत्रित किया जा सकता है",
      "हर कोई एक पासवर्ड साझा कर सकता है",
      "यह सुरक्षा की आवश्यकता को समाप्त करता है",
      "यह सभी रिकॉर्ड सार्वजनिक बनाता है"
    ],
    "answer": "Actions can be linked to the correct account and access can be controlled",
    "correctAnswerIndex": 0,
    "explanation": "Individual accountability ensures audit logging can attribute activities to specific persons.",
    "explanation_en": "Actions can be linked to the correct account and access can be controlled.",
    "explanation_hi": "अलग-अलग खाते होने से यह पता चलता है कि किस छात्र ने क्या काम किया और सुरक्षा बेहतर रहती है।"
  },
  {
    "id": "L4_T1_SCH_05",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "What does multi-factor authentication use?",
    "question_en": "What does multi-factor authentication use?",
    "question_hi": "मल्टी-फ़ैक्टर ऑथेंटिकेशन (MFA) में किसका उपयोग किया जाता है?",
    "options": [
      "Two or more different types of proof",
      "Two usernames only",
      "Two copies of the same password only",
      "A password written on paper"
    ],
    "options_en": [
      "Two or more different types of proof",
      "Two usernames only",
      "Two copies of the same password only",
      "A password written on paper"
    ],
    "options_hi": [
      "पहचान के दो या दो से अधिक अलग-अलग प्रकार के प्रमाण (जैसे पासवर्ड + OTP)",
      "केवल दो उपयोगकर्ता नाम",
      "एक ही पासवर्ड की केवल दो प्रतियां",
      "कागज पर लिखा पासवर्ड"
    ],
    "answer": "Two or more different types of proof",
    "correctAnswerIndex": 0,
    "explanation": "MFA combines factors across something you know (password), have (phone/token), or are (fingerprint).",
    "explanation_en": "Two or more different types of proof.",
    "explanation_hi": "MFA में लॉगिन के लिए पासवर्ड के साथ-साथ मोबाइल OTP या फिंगरप्रिंट जैसे अतिरिक्त प्रमाण की ज़रूरत होती है।"
  },
  {
    "id": "L4_T1_SCH_06",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "What should happen to an account when its owner no longer needs access?",
    "question_en": "What should happen to an account when its owner no longer needs access?",
    "question_hi": "जब किसी खाताधारक को अब एक्सेस की आवश्यकता नहीं होती (जैसे स्कूल छोड़ना), तो खाते का क्या होना चाहिए?",
    "options": [
      "Access should be reviewed and removed when appropriate",
      "It should stay active forever",
      "Its password should be posted publicly",
      "It should be shared with strangers"
    ],
    "options_en": [
      "Access should be reviewed and removed when appropriate",
      "It should stay active forever",
      "Its password should be posted publicly",
      "It should be shared with strangers"
    ],
    "options_hi": [
      "पहुँच की समीक्षा की जानी चाहिए और उपयुक्त होने पर उसे निष्क्रिय/हटा दिया जाना चाहिए",
      "इसे हमेशा के लिए सक्रिय रहना चाहिए",
      "इसका पासवर्ड सार्वजनिक रूप से पोस्ट किया जाना चाहिए",
      "इसे अजनबियों के साथ साझा किया जाना चाहिए"
    ],
    "answer": "Access should be reviewed and removed when appropriate",
    "correctAnswerIndex": 0,
    "explanation": "Deprovisioning inactive accounts stops orphaned credentials from being hijacked by attackers.",
    "explanation_en": "Access should be reviewed and removed when appropriate.",
    "explanation_hi": "निष्क्रिय खातों को बंद करना आवश्यक है ताकि कोई उनका दुरुपयोग न कर सके।"
  },
  {
    "id": "L4_T1_SCH_07",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "Which is an example of something you have for authentication?",
    "question_en": "Which is an example of something you have for authentication?",
    "question_hi": "प्रमाणीकरण में 'कोई वस्तु जो आपके पास है' (Something you have) का उदाहरण कौन सा है?",
    "options": [
      "A security key or registered phone",
      "Your favourite colour",
      "A public poster",
      "A website logo"
    ],
    "options_en": [
      "A security key or registered phone",
      "Your favourite colour",
      "A public poster",
      "A website logo"
    ],
    "options_hi": [
      "एक भौतिक सुरक्षा कुंजी (Security Key) या पंजीकृत मोबाइल फ़ोन",
      "आपका पसंदीदा रंग",
      "एक सार्वजनिक पोस्टर",
      "एक वेबसाइट लोगो"
    ],
    "answer": "A security key or registered phone",
    "correctAnswerIndex": 0,
    "explanation": "Possession factors include hardware tokens, smartphones receiving push prompts, and smartcards.",
    "explanation_en": "A security key or registered phone.",
    "explanation_hi": "मोबाइल फोन, हार्डवेयर टोकन या स्मार्टकार्ड भौतिक वस्तुएं हैं जो उपयोगकर्ता की पहचान प्रमाणित करती हैं।"
  },
  {
    "id": "L4_T1_SCH_08",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "Why are shared administrator accounts risky?",
    "question_en": "Why are shared administrator accounts risky?",
    "question_hi": "साझा व्यवस्थापक खाते (Shared Admin Accounts) जोखिम भरे क्यों होते हैं?",
    "options": [
      "It is harder to identify who performed an action and control access",
      "They always improve security",
      "They create automatic backups",
      "They prevent phishing"
    ],
    "options_en": [
      "It is harder to identify who performed an action and control access",
      "They always improve security",
      "They create automatic backups",
      "They prevent phishing"
    ],
    "options_hi": [
      "यह पहचानना कठिन होता है कि किसने कौन सी कार्रवाई की और पहुँच को नियंत्रित करना मुश्किल हो जाता है",
      "वे हमेशा सुरक्षा में सुधार करते हैं",
      "वे स्वचालित बैकअप बनाते हैं",
      "वे फ़िशिंग को रोकते हैं"
    ],
    "answer": "It is harder to identify who performed an action and control access",
    "correctAnswerIndex": 0,
    "explanation": "Shared accounts ruin audit trails and make password rotation virtually impossible when staff depart.",
    "explanation_en": "It is harder to identify who performed an action and control access.",
    "explanation_hi": "एक ही एडमिन पासवर्ड कई लोगों के पास होने पर यह साबित नहीं किया जा सकता कि गलती या बदलाव किसने किया।"
  },
  {
    "id": "L4_T1_SCH_09",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "What is single sign-on (SSO)?",
    "question_en": "What is single sign-on (SSO)?",
    "question_hi": "सिंगल साइन-ऑन (SSO - Single Sign-On) क्या है?",
    "options": [
      "A system that lets a user access multiple approved services through one sign-in process",
      "Using one weak password everywhere without controls",
      "Logging in without identity checks",
      "Sharing a login with classmates"
    ],
    "options_en": [
      "A system that lets a user access multiple approved services through one sign-in process",
      "Using one weak password everywhere without controls",
      "Logging in without identity checks",
      "Sharing a login with classmates"
    ],
    "options_hi": [
      "एक ऐसी प्रणाली जो उपयोगकर्ता को एक ही सुरक्षित साइन-इन प्रक्रिया से कई स्वीकृत सेवाओं तक पहुँचने देती है",
      "बिना किसी नियंत्रण के हर जगह एक ही कमजोर पासवर्ड का उपयोग करना",
      "पहचान जांच के बिना लॉगिन करना",
      "सहपाठियों के साथ लॉगिन साझा करना"
    ],
    "answer": "A system that lets a user access multiple approved services through one sign-in process",
    "correctAnswerIndex": 0,
    "explanation": "SSO centralizes identity verification, allowing one secure authentication to federate access across apps.",
    "explanation_en": "A system that lets a user access multiple approved services through one sign-in process.",
    "explanation_hi": "SSO के माध्यम से एक बार सुरक्षित लॉगिन करके स्कूल की सभी वेबसाइटों और ऐप्स को खोला जा सकता है।"
  },
  {
    "id": "L4_T1_SCH_10",
    "level": 4,
    "topic": "Identity-Based Architecture",
    "topicId": "identity_based_architecture",
    "mode": "school",
    "question": "Why should identity permissions be reviewed regularly?",
    "question_en": "Why should identity permissions be reviewed regularly?",
    "question_hi": "उपयोगकर्ताओं की अनुमतियों (Permissions) की नियमित समीक्षा क्यों की जानी चाहिए?",
    "options": [
      "People's roles and access needs can change",
      "Passwords stop working every day",
      "It makes all data public",
      "It removes the need for authentication"
    ],
    "options_en": [
      "People's roles and access needs can change",
      "Passwords stop working every day",
      "It makes all data public",
      "It removes the need for authentication"
    ],
    "options_hi": [
      "लोगों की भूमिकाएं, कक्षाएं और पहुँच की आवश्यकताएं समय के साथ बदल सकती हैं",
      "पासवर्ड हर दिन काम करना बंद कर देते हैं",
      "यह सभी डेटा को सार्वजनिक करता है",
      "यह प्रमाणीकरण की आवश्यकता को हटाता है"
    ],
    "answer": "People's roles and access needs can change",
    "correctAnswerIndex": 0,
    "explanation": "Periodic access reviews prevent privilege creep where users accumulate unneeded elevated permissions.",
    "explanation_en": "People's roles and access needs can change.",
    "explanation_hi": "छात्रों के अगली कक्षा में जाने या शिक्षकों की जिम्मेदारी बदलने पर पुरानी अनुमतियों को अपडेट करना ज़रूरी होता है।"
  },

  # Topic 17 (L4 T2): Device-Based Architecture
  {
    "id": "L4_T2_SCH_01",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Why should laptops and phones be locked when unattended?",
    "question_en": "Why should laptops and phones be locked when unattended?",
    "question_hi": "लैपटॉप और फोन को लावारिस छोड़ते समय स्क्रीन लॉक क्यों किया जाना चाहिए?",
    "options": [
      "To prevent unauthorized people from accessing them",
      "To improve speaker volume",
      "To make Wi-Fi public",
      "To remove installed updates"
    ],
    "options_en": [
      "To prevent unauthorized people from accessing them",
      "To improve speaker volume",
      "To make Wi-Fi public",
      "To remove installed updates"
    ],
    "options_hi": [
      "अनधिकृत व्यक्तियों को उन तक पहुँचने और डेटा चुराने से रोकने के लिए",
      "स्पीकर की आवाज़ बढ़ाने के लिए",
      "वाई-फ़ाई को सार्वजनिक करने के लिए",
      "इंस्टॉल किए गए अपडेट को हटाने के लिए"
    ],
    "answer": "To prevent unauthorized people from accessing them",
    "correctAnswerIndex": 0,
    "explanation": "Locking screens prevents opportunistic physical snooping and unauthorized local access.",
    "explanation_en": "To prevent unauthorized people from accessing them.",
    "explanation_hi": "डिवाइस लॉक रखने से कोई दूसरा व्यक्ति आपकी अनुपस्थिति में आपके ईमेल, चैट या निजी फ़ाइलें नहीं देख सकता।"
  },
  {
    "id": "L4_T2_SCH_02",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "What is device encryption useful for?",
    "question_en": "What is device encryption useful for?",
    "question_hi": "डिवाइस एन्क्रिप्शन (Device Encryption) किसलिए उपयोगी है?",
    "options": [
      "Making stored data harder to read without the correct key or access",
      "Increasing screen brightness",
      "Making all websites safe",
      "Stopping every scam message"
    ],
    "options_en": [
      "Making stored data harder to read without the correct key or access",
      "Increasing screen brightness",
      "Making all websites safe",
      "Stopping every scam message"
    ],
    "options_hi": [
      "सही सुरक्षा कुंजी या पासवर्ड के बिना संग्रहीत डेटा को पढ़ने में असमर्थ बनाना",
      "स्क्रीन की चमक बढ़ाना",
      "सभी वेबसाइटों को सुरक्षित बनाना",
      "हर घोटाले वाले संदेश को रोकना"
    ],
    "answer": "Making stored data harder to read without the correct key or access",
    "correctAnswerIndex": 0,
    "explanation": "Full disk encryption (BitLocker, FileVault) scrambles files so thieves cannot read data off stolen drives.",
    "explanation_en": "Making stored data harder to read without the correct key or access.",
    "explanation_hi": "एन्क्रिप्शन डेटा को एक गुप्त कोड में बदल देता है, जिससे लैपटॉप चोरी होने पर भी चोर उसमें मौजूद फ़ाइलें नहीं पढ़ सकता।"
  },
  {
    "id": "L4_T2_SCH_03",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Why should operating systems receive security updates?",
    "question_en": "Why should operating systems receive security updates?",
    "question_hi": "ऑपरेटिंग सिस्टम को नियमित सुरक्षा अपडेट क्यों प्राप्त होने चाहिए?",
    "options": [
      "Updates can fix known weaknesses",
      "Updates make passwords unnecessary",
      "Updates stop all human mistakes",
      "Updates publish private files"
    ],
    "options_en": [
      "Updates can fix known weaknesses",
      "Updates make passwords unnecessary",
      "Updates stop all human mistakes",
      "Updates publish private files"
    ],
    "options_hi": [
      "अपडेट ज्ञात सुरक्षा कमज़ोरियों (Vulnerabilities) और बग्स को ठीक करते हैं",
      "अपडेट पासवर्ड को अनावश्यक बनाते हैं",
      "अपडेट सभी मानवीय गलतियों को रोकते हैं",
      "अपडेट निजी फ़ाइलें प्रकाशित करते हैं"
    ],
    "answer": "Updates can fix known weaknesses",
    "correctAnswerIndex": 0,
    "explanation": "OS patches repair software flaws that could otherwise be targeted by automated exploits and malware.",
    "explanation_en": "Updates can fix known weaknesses.",
    "explanation_hi": "ऑपरेटिंग सिस्टम के अपडेट सिस्टम की सुरक्षा कमज़ोरियों को ठीक करते हैं ताकि हैकर उनका फायदा न उठा सकें।"
  },
  {
    "id": "L4_T2_SCH_04",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "What should you do before connecting an unknown USB drive?",
    "question_en": "What should you do before connecting an unknown USB drive?",
    "question_hi": "किसी अनजान USB ड्राइव (पेन ड्राइव) को कनेक्ट करने से पहले आपको क्या करना चाहिए?",
    "options": [
      "Avoid using it until it can be checked safely",
      "Open every file immediately",
      "Disable antivirus",
      "Copy it to every computer"
    ],
    "options_en": [
      "Avoid using it until it can be checked safely",
      "Open every file immediately",
      "Disable antivirus",
      "Copy it to every computer"
    ],
    "options_hi": [
      "जब तक इसे सुरक्षित रूप से जाँचा न जा सके, इसके उपयोग से बचें",
      "तुरंत हर फ़ाइल खोलें",
      "एंटीवायरस अक्षम करें",
      "इसे हर कंप्यूटर में कॉपी करें"
    ],
    "answer": "Avoid using it until it can be checked safely",
    "correctAnswerIndex": 0,
    "explanation": "Unknown USB drives may carry BadUSB firmware or autorun malware designed to compromise systems.",
    "explanation_en": "Avoid using it until it can be checked safely.",
    "explanation_hi": "सड़क पर मिली या अनजान पेन ड्राइव में मैलवेयर हो सकता है, इसलिए उसे बिना स्कैन किए कभी नहीं लगाना चाहिए।"
  },
  {
    "id": "L4_T2_SCH_05",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "What is endpoint security?",
    "question_en": "What is endpoint security?",
    "question_hi": "एंडपॉइंट सुरक्षा (Endpoint Security) क्या है?",
    "options": [
      "Protecting devices such as laptops, phones, and servers",
      "Protecting only the end of a desk",
      "A way to make a password public",
      "A type of screen brightness"
    ],
    "options_en": [
      "Protecting devices such as laptops, phones, and servers",
      "Protecting only the end of a desk",
      "A way to make a password public",
      "A type of screen brightness"
    ],
    "options_hi": [
      "लैपटॉप, मोबाइल फ़ोन और सर्वर जैसे नेटवर्क से जुड़े सभी उपकरणों की सुरक्षा करना",
      "केवल डेस्क के छोर की रक्षा करना",
      "पासवर्ड को सार्वजनिक करने का एक तरीका",
      "स्क्रीन की चमक का एक प्रकार"
    ],
    "answer": "Protecting devices such as laptops, phones, and servers",
    "correctAnswerIndex": 0,
    "explanation": "Endpoint security safeguards end-user devices (laptops, mobiles) from zero-day threats and malware.",
    "explanation_en": "Protecting devices such as laptops, phones, and servers.",
    "explanation_hi": "एंडपॉइंट सुरक्षा का अर्थ नेटवर्क से जुड़े हर अंतिम डिवाइस (कंप्यूटर, स्मार्टफोन आदि) की सुरक्षा करना है।"
  },
  {
    "id": "L4_T2_SCH_06",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Why might a school restrict which apps can be installed on its devices?",
    "question_en": "Why might a school restrict which apps can be installed on its devices?",
    "question_hi": "एक स्कूल अपने कंप्यूटरों और उपकरणों पर इंस्टॉल किए जा सकने वाले ऐप्स को प्रतिबंधित क्यों कर सकता है?",
    "options": [
      "To reduce unsafe or unauthorized software",
      "To make every app safe automatically",
      "To stop all learning",
      "To share administrator accounts"
    ],
    "options_en": [
      "To reduce unsafe or unauthorized software",
      "To make every app safe automatically",
      "To stop all learning",
      "To share administrator accounts"
    ],
    "options_hi": [
      "असुरक्षित, हानिकारक या अनधिकृत सॉफ़्टवेयर के जोखिम को कम करने के लिए",
      "हर ऐप को अपने आप सुरक्षित बनाने के लिए",
      "सभी प्रकार की पढ़ाई रोकने के लिए",
      "व्यवस्थापक खातों को साझा करने के लिए"
    ],
    "answer": "To reduce unsafe or unauthorized software",
    "correctAnswerIndex": 0,
    "explanation": "Application whitelisting stops untrusted, malicious, or non-educational software from running.",
    "explanation_en": "To reduce unsafe or unauthorized software.",
    "explanation_hi": "अनधिकृत ऐप्स डाउनलोड करने पर रोक लगाने से स्कूल के कंप्यूटर वायरस और मैलवेयर से सुरक्षित रहते हैं।"
  },
  {
    "id": "L4_T2_SCH_07",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "What should you do if your school laptop is lost?",
    "question_en": "What should you do if your school laptop is lost?",
    "question_hi": "यदि आपका स्कूल का लैपटॉप खो जाता है, तो आपको क्या करना चाहिए?",
    "options": [
      "Report it promptly so the school can protect accounts and data",
      "Wait several weeks",
      "Post its password online",
      "Ignore the loss"
    ],
    "options_en": [
      "Report it promptly so the school can protect accounts and data",
      "Wait several weeks",
      "Post its password online",
      "Ignore the loss"
    ],
    "options_hi": [
      "तुरंत इसकी सूचना दें ताकि स्कूल खातों और संवेदनशील डेटा को सुरक्षित/लॉक कर सके",
      "कई हफ्तों तक प्रतीक्षा करें",
      "इसका पासवर्ड ऑनलाइन पोस्ट करें",
      "नुकसान को अनदेखा करें"
    ],
    "answer": "Report it promptly so the school can protect accounts and data",
    "correctAnswerIndex": 0,
    "explanation": "Immediate notification allows IT administrators to remotely lock the device and invalidate session tokens.",
    "explanation_en": "Report it promptly so the school can protect accounts and data.",
    "explanation_hi": "लैपटॉप खोने की तुरंत सूचना देने से IT टीम रिमोटली उसका डेटा मिटा सकती है और खातों को सुरक्षित कर सकती है।"
  },
  {
    "id": "L4_T2_SCH_08",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Why is automatic screen locking useful?",
    "question_en": "Why is automatic screen locking useful?",
    "question_hi": "स्वचालित स्क्रीन लॉक (Automatic Screen Locking) क्यों उपयोगी है?",
    "options": [
      "It protects an unattended device after a period of inactivity",
      "It deletes all malware",
      "It makes every file public",
      "It removes the need for updates"
    ],
    "options_en": [
      "It protects an unattended device after a period of inactivity",
      "It deletes all malware",
      "It makes every file public",
      "It removes the need for updates"
    ],
    "options_hi": [
      "यह कुछ समय तक इस्तेमाल न होने पर लावारिस डिवाइस को अपने आप लॉक करके सुरक्षित करता है",
      "यह सभी मैलवेयर को हटा देता है",
      "यह हर फ़ाइल को सार्वजनिक बनाता है",
      "यह अपडेट की आवश्यकता को समाप्त करता है"
    ],
    "answer": "It protects an unattended device after a period of inactivity",
    "correctAnswerIndex": 0,
    "explanation": "Inactivity timeouts ensure computers lock automatically if a user walks away without manual locking.",
    "explanation_en": "It protects an unattended device after a period of inactivity.",
    "explanation_hi": "यदि आप कंप्यूटर खुला छोड़कर चले जाते हैं, तो ऑटो-लॉक कुछ ही मिनटों में स्क्रीन बंद करके दूसरों की पहुँच रोक देता है।"
  },
  {
    "id": "L4_T2_SCH_09",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Which is safer for installing apps?",
    "question_en": "Which is safer for installing apps?",
    "question_hi": "ऐप्स इंस्टॉल करने के लिए इनमें से कौन सा तरीका अधिक सुरक्षित है?",
    "options": [
      "An official or organization-approved source",
      "A random pop-up download",
      "A link from an unknown stranger",
      "A cracked software site"
    ],
    "options_en": [
      "An official or organization-approved source",
      "A random pop-up download",
      "A link from an unknown stranger",
      "A cracked software site"
    ],
    "options_hi": [
      "एक आधिकारिक या स्कूल द्वारा अनुमोदित ऐप स्टोर/स्रोत",
      "एक यादृच्छिक पॉप-अप विज्ञापन से डाउनलोड",
      "किसी अज्ञात अजनबी से प्राप्त लिंक",
      "क्रैक किए गए सॉफ़्टवेयर की साइट"
    ],
    "answer": "An official or organization-approved source",
    "correctAnswerIndex": 0,
    "explanation": "Vetted software repositories digitally sign and scan packages before making them available.",
    "explanation_en": "An official or organization-approved source.",
    "explanation_hi": "आधिकारिक स्टोर पर उपलब्ध ऐप्स की पहले से सुरक्षा जांच की जाती है, जिससे वे सुरक्षित होते हैं।"
  },
  {
    "id": "L4_T2_SCH_10",
    "level": 4,
    "topic": "Device-Based Architecture",
    "topicId": "device_based_architecture",
    "mode": "school",
    "question": "Why should security tools on devices be kept enabled?",
    "question_en": "Why should security tools on devices be kept enabled?",
    "question_hi": "डिवाइस पर सुरक्षा उपकरणों (Antivirus/Firewall) को हमेशा सक्रिय क्यों रखना चाहिए?",
    "options": [
      "They can help detect threats and enforce protective settings",
      "They guarantee zero risk",
      "They replace every backup",
      "They make sharing passwords safe"
    ],
    "options_en": [
      "They can help detect threats and enforce protective settings",
      "They guarantee zero risk",
      "They replace every backup",
      "They make sharing passwords safe"
    ],
    "options_hi": [
      "वे खतरों का समय पर पता लगाने और सुरक्षा सेटिंग्स को लागू करने में मदद करते हैं",
      "वे शून्य जोखिम की गारंटी देते हैं",
      "वे प्रत्येक बैकअप की जगह लेते हैं",
      "वे पासवर्ड साझा करना सुरक्षित बनाते हैं"
    ],
    "answer": "They can help detect threats and enforce protective settings",
    "correctAnswerIndex": 0,
    "explanation": "Active endpoint agents perform continuous real-time behavioral monitoring and exploit prevention.",
    "explanation_en": "They can help detect threats and enforce protective settings.",
    "explanation_hi": "सुरक्षा टूल्स चालू रहने पर वायरस, स्पायवेयर और दुर्भावनापूर्ण नेटवर्क हमलों को तुरंत ब्लॉक कर देते हैं।"
  },

  # Topic 18 (L4 T3): Network-Based Architecture
  {
    "id": "L4_T3_SCH_01",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "What is a computer network?",
    "question_en": "What is a computer network?",
    "question_hi": "कंप्यूटर नेटवर्क (Computer Network) क्या है?",
    "options": [
      "Connected devices that communicate and share resources",
      "A group of unrelated paper books",
      "A single keyboard key",
      "A type of battery"
    ],
    "options_en": [
      "Connected devices that communicate and share resources",
      "A group of unrelated paper books",
      "A single keyboard key",
      "A type of battery"
    ],
    "options_hi": [
      "आपस में जुड़े हुए उपकरण जो एक दूसरे के साथ संचार करते हैं और संसाधन साझा करते हैं",
      "असंबंधित कागज़ की किताबों का एक समूह",
      "एक एकल कीबोर्ड कुंजी",
      "एक प्रकार की बैटरी"
    ],
    "answer": "Connected devices that communicate and share resources",
    "correctAnswerIndex": 0,
    "explanation": "A computer network links multiple computing endpoints to enable data exchange and resource sharing.",
    "explanation_en": "Connected devices that communicate and share resources.",
    "explanation_hi": "कंप्यूटर नेटवर्क कई कंप्यूटरों और उपकरणों का समूह है जो डेटा और प्रिंटर/इंटरनेट जैसे संसाधनों को साझा करते हैं।"
  },
  {
    "id": "L4_T3_SCH_02",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "Why might a school separate guest Wi-Fi from its internal network?",
    "question_en": "Why might a school separate guest Wi-Fi from its internal network?",
    "question_hi": "एक स्कूल अपने गेस्ट (अतिथि) वाई-फ़ाई को आंतरिक प्रशासनिक नेटवर्क से अलग क्यों रखता है?",
    "options": [
      "To limit guests' access to important systems",
      "To give guests every administrator permission",
      "To remove all passwords",
      "To disable the internet permanently"
    ],
    "options_en": [
      "To limit guests' access to important systems",
      "To give guests every administrator permission",
      "To remove all passwords",
      "To disable the internet permanently"
    ],
    "options_hi": [
      "महत्वपूर्ण आंतरिक स्कूल प्रणालियों और प्रशासनिक रिकॉर्ड तक अतिथियों की पहुँच को रोकने के लिए",
      "अतिथियों को हर व्यवस्थापक अनुमति देने के लिए",
      "सभी पासवर्ड हटाने के लिए",
      "इंटरनेट को स्थायी रूप से अक्षम करने के लिए"
    ],
    "answer": "To limit guests' access to important systems",
    "correctAnswerIndex": 0,
    "explanation": "Network segmentation keeps untrusted guest devices isolated from internal servers and sensitive databases.",
    "explanation_en": "To limit guests' access to important systems.",
    "explanation_hi": "गेस्ट नेटवर्क को अलग रखने से आगंतुक या छात्र स्कूल के मुख्य प्रशासनिक सर्वर और परीक्षा रिकॉर्ड तक नहीं पहुँच सकते।"
  },
  {
    "id": "L4_T3_SCH_03",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "What does a router commonly do?",
    "question_en": "What does a router commonly do?",
    "question_hi": "एक राउटर (Router) आमतौर पर क्या कार्य करता है?",
    "options": [
      "Forwards data between networks",
      "Scans paper documents only",
      "Stores every password publicly",
      "Replaces all user accounts"
    ],
    "options_en": [
      "Forwards data between networks",
      "Scans paper documents only",
      "Stores every password publicly",
      "Replaces all user accounts"
    ],
    "options_hi": [
      "विभिन्न नेटवर्क के बीच डेटा पैकेट को सही गंतव्य तक पहुँचाता है (Forward करता है)",
      "केवल कागज़ी दस्तावेज़ों को स्कैन करता है",
      "हर पासवर्ड को सार्वजनिक रूप से स्टोर करता है",
      "सभी उपयोगकर्ता खातों को बदल देता है"
    ],
    "answer": "Forwards data between networks",
    "correctAnswerIndex": 0,
    "explanation": "Routers direct IP packets across interconnected local and wide area networks using routing tables.",
    "explanation_en": "Forwards data between networks.",
    "explanation_hi": "राउटर डेटा पैकेट्स को एक नेटवर्क से दूसरे नेटवर्क (जैसे आपके घर के नेटवर्क से इंटरनेट) तक सही रास्ते से भेजता है।"
  },
  {
    "id": "L4_T3_SCH_04",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "What is an IP address used for?",
    "question_en": "What is an IP address used for?",
    "question_hi": "आईपी एड्रेस (IP Address) का उपयोग किसलिए किया जाता है?",
    "options": [
      "Identifying a network interface for communication",
      "Measuring a screen",
      "Choosing a password's colour",
      "Charging a device"
    ],
    "options_en": [
      "Identifying a network interface for communication",
      "Measuring a screen",
      "Choosing a password's colour",
      "Charging a device"
    ],
    "options_hi": [
      "नेटवर्क संचार के लिए किसी डिवाइस या नेटवर्क इंटरफ़ेस की विशिष्ट पहचान करने के लिए",
      "स्क्रीन को मापने के लिए",
      "पासवर्ड का रंग चुनने के लिए",
      "डिवाइस को चार्ज करने के लिए"
    ],
    "answer": "Identifying a network interface for communication",
    "correctAnswerIndex": 0,
    "explanation": "An IP address uniquely identifies each connected node on an IP network to route communication packets.",
    "explanation_en": "Identifying a network interface for communication.",
    "explanation_hi": "जैसे घर का पता होता है, वैसे ही इंटरनेट पर हर कंप्यूटर का एक विशिष्ट IP एड्रेस होता है ताकि डेटा सही जगह पहुँचे।"
  },
  {
    "id": "L4_T3_SCH_05",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "Why should default passwords on network devices be changed?",
    "question_en": "Why should default passwords on network devices be changed?",
    "question_hi": "नेटवर्क उपकरणों (जैसे राउटर या वाई-फ़ाई) के डिफ़ॉल्ट पासवर्ड को क्यों बदल देना चाहिए?",
    "options": [
      "They may be widely known or easy to guess",
      "They always use too much battery",
      "They prevent updates",
      "They make cables shorter"
    ],
    "options_en": [
      "They may be widely known or easy to guess",
      "They always use too much battery",
      "They prevent updates",
      "They make cables shorter"
    ],
    "options_hi": [
      "वे व्यापक रूप से इंटरनेट पर सार्वजनिक होते हैं और हमलावर उनका आसानी से अनुमान लगा सकते हैं",
      "वे हमेशा बहुत अधिक बैटरी का उपयोग करते हैं",
      "वे अपडेट को रोकते हैं",
      "वे केबल को छोटा बनाते हैं"
    ],
    "answer": "They may be widely known or easy to guess",
    "correctAnswerIndex": 0,
    "explanation": "Default credentials (like admin/admin) are published in online databases and actively targeted by bots.",
    "explanation_en": "They may be widely known or easy to guess.",
    "explanation_hi": "राउटर के साथ आने वाले डिफ़ॉल्ट पासवर्ड (जैसे admin/admin) सबको पता होते हैं, जिन्हें बदलकर मजबूत पासवर्ड लगाना ज़रूरी है।"
  },
  {
    "id": "L4_T3_SCH_06",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "What is network segmentation?",
    "question_en": "What is network segmentation?",
    "question_hi": "नेटवर्क सेगमेंटेशन (Network Segmentation) क्या है?",
    "options": [
      "Dividing a network into separate sections to control traffic",
      "Putting every device on one open network",
      "Deleting all network cables",
      "Making every file public"
    ],
    "options_en": [
      "Dividing a network into separate sections to control traffic",
      "Putting every device on one open network",
      "Deleting all network cables",
      "Making every file public"
    ],
    "options_hi": [
      "ट्रैफ़िक और सुरक्षा को नियंत्रित करने के लिए नेटवर्क को अलग-अलग उप-वर्गों (Subnets) में विभाजित करना",
      "हर डिवाइस को एक ही खुले नेटवर्क पर रखना",
      "सभी नेटवर्क केबल हटाना",
      "हर फ़ाइल को सार्वजनिक करना"
    ],
    "answer": "Dividing a network into separate sections to control traffic",
    "correctAnswerIndex": 0,
    "explanation": "Segmentation isolates critical subnetworks using VLANs and firewalls, stopping the lateral spread of malware.",
    "explanation_en": "Dividing a network into separate sections to control traffic.",
    "explanation_hi": "नेटवर्क को अलग-अलग हिस्सों में बांटने से अगर एक कंप्यूटर में वायरस आ भी जाए, तो वह दूसरे महत्वपूर्ण सर्वर में नहीं फैल सकता।"
  },
  {
    "id": "L4_T3_SCH_07",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "Which device commonly directs traffic between different networks?",
    "question_en": "Which device commonly directs traffic between different networks?",
    "question_hi": "विभिन्न नेटवर्कों के बीच ट्रैफ़िक को कौन सा उपकरण निर्देशित करता है?",
    "options": [
      "Router",
      "Mouse",
      "Webcam",
      "Microphone"
    ],
    "options_en": [
      "Router",
      "Mouse",
      "Webcam",
      "Microphone"
    ],
    "options_hi": [
      "राउटर (Router)",
      "माउस (Mouse)",
      "वेबकैम (Webcam)",
      "माइक्रोफ़ोन (Microphone)"
    ],
    "answer": "Router",
    "correctAnswerIndex": 0,
    "explanation": "Routers operate at the Network Layer (Layer 3) to route packets across separate subnetworks.",
    "explanation_en": "Router.",
    "explanation_hi": "राउटर ही वह मुख्य उपकरण है जो अलग-अलग नेटवर्कों के बीच इंटरनेट ट्रैफ़िक का आदान-प्रदान कराता है।"
  },
  {
    "id": "L4_T3_SCH_08",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "Why monitor network traffic?",
    "question_en": "Why monitor network traffic?",
    "question_hi": "नेटवर्क ट्रैफ़िक की निगरानी (Traffic Monitoring) क्यों की जाती है?",
    "options": [
      "To help notice unusual activity or possible attacks",
      "To collect passwords for public sharing",
      "To stop every software bug",
      "To change screen resolution"
    ],
    "options_en": [
      "To help notice unusual activity or possible attacks",
      "To collect passwords for public sharing",
      "To stop every software bug",
      "To change screen resolution"
    ],
    "options_hi": [
      "असामान्य गतिविधि, घुसपैठ या संभावित साइबर हमलों का तुरंत पता लगाने के लिए",
      "सार्वजनिक साझाकरण के लिए पासवर्ड एकत्र करने के लिए",
      "प्रत्येक सॉफ़्टवेयर बग को रोकने के लिए",
      "स्क्रीन रिज़ॉल्यूशन बदलने के लिए"
    ],
    "answer": "To help notice unusual activity or possible attacks",
    "correctAnswerIndex": 0,
    "explanation": "Continuous traffic telemetry highlights abnormal data spikes, port scans, and command-and-control beacons.",
    "explanation_en": "To help notice unusual activity or possible attacks.",
    "explanation_hi": "नेटवर्क ट्रैफ़िक पर नज़र रखने से किसी हैकर की घुसपैठ या डेटा चोरी की कोशिश तुरंत पकड़ी जा सकती है।"
  },
  {
    "id": "L4_T3_SCH_09",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "What should be done with unused network services?",
    "question_en": "What should be done with unused network services?",
    "question_hi": "अप्रयुक्त या गैर-ज़रूरी नेटवर्क सेवाओं (Unused Services) का क्या किया जाना चाहिए?",
    "options": [
      "Disable them when appropriate to reduce exposure",
      "Open them to everyone",
      "Share their passwords publicly",
      "Ignore their settings forever"
    ],
    "options_en": [
      "Disable them when appropriate to reduce exposure",
      "Open them to everyone",
      "Share their passwords publicly",
      "Ignore their settings forever"
    ],
    "options_hi": [
      "सुरक्षा जोखिम को कम करने के लिए उन्हें अक्षम (Disable/बंद) कर देना चाहिए",
      "उन्हें सभी के लिए खुला रखें",
      "उनके पासवर्ड सार्वजनिक रूप से साझा करें",
      "उनकी सेटिंग्स को हमेशा के लिए अनदेखा करें"
    ],
    "answer": "Disable them when appropriate to reduce exposure",
    "correctAnswerIndex": 0,
    "explanation": "Disabling unneeded daemons and ports minimizes the system attack surface according to hardening benchmarks.",
    "explanation_en": "Disable them when appropriate to reduce exposure.",
    "explanation_hi": "जिन सेवाओं की ज़रूरत न हो उन्हें बंद रखने से हमलावरों के लिए घुसपैठ के रास्ते बंद हो जाते हैं।"
  },
  {
    "id": "L4_T3_SCH_10",
    "level": 4,
    "topic": "Network-Based Architecture",
    "topicId": "network_based_architecture",
    "mode": "school",
    "question": "Who should change important network settings in a school?",
    "question_en": "Who should change important network settings in a school?",
    "question_hi": "स्कूल में महत्वपूर्ण नेटवर्क सेटिंग्स को बदलने का अधिकार किसे होना चाहिए?",
    "options": [
      "Authorized network or IT staff",
      "Any visitor",
      "An unknown caller",
      "A random social media account"
    ],
    "options_en": [
      "Authorized network or IT staff",
      "Any visitor",
      "An unknown caller",
      "A random social media account"
    ],
    "options_hi": [
      "केवल अधिकृत नेटवर्क या IT विभाग के कर्मचारी",
      "कोई भी आगंतुक",
      "एक अज्ञात कॉलर",
      "एक यादृच्छिक सोशल मीडिया खाता"
    ],
    "answer": "Authorized network or IT staff",
    "correctAnswerIndex": 0,
    "explanation": "Network infrastructure control must be strictly restricted to trained and accountable administrators.",
    "explanation_en": "Authorized network or IT staff.",
    "explanation_hi": "स्कूल के इंटरनेट और राउटर की सेटिंग्स केवल अधिकृत IT एडमिनिस्ट्रेटर ही बदल सकते हैं।"
  },

  # Topic 19 (L4 T4): Data-Centric Architecture
  {
    "id": "L4_T4_SCH_01",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "What does data-centric security focus on?",
    "question_en": "What does data-centric security focus on?",
    "question_hi": "डेटा-केंद्रित सुरक्षा (Data-Centric Security) किस पर ध्यान केंद्रित करती है?",
    "options": [
      "Protecting the information itself wherever it is stored or used",
      "Protecting only the computer's colour",
      "Making all information public",
      "Changing screen brightness"
    ],
    "options_en": [
      "Protecting the information itself wherever it is stored or used",
      "Protecting only the computer's colour",
      "Making all information public",
      "Changing screen brightness"
    ],
    "options_hi": [
      "डेटा और जानकारी की स्वयं सुरक्षा करना, चाहे वह कहीं भी संग्रहीत या उपयोग की जा रही हो",
      "केवल कंप्यूटर के रंग की रक्षा करना",
      "सभी जानकारी को सार्वजनिक करना",
      "स्क्रीन की चमक बदलना"
    ],
    "answer": "Protecting the information itself wherever it is stored or used",
    "correctAnswerIndex": 0,
    "explanation": "Data-centric security attaches protection policies (like encryption and access rights) directly to the data.",
    "explanation_en": "Protecting the information itself wherever it is stored or used.",
    "explanation_hi": "डेटा-केंद्रित सुरक्षा में केवल नेटवर्क की नहीं, बल्कि स्वयं फ़ाइलों और डेटा को एन्क्रिप्ट करके सुरक्षित रखा जाता है।"
  },
  {
    "id": "L4_T4_SCH_02",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "What does encryption do?",
    "question_en": "What does encryption do?",
    "question_hi": "एन्क्रिप्शन (Encryption) क्या करता है?",
    "options": [
      "Transforms readable information into protected form that needs a key to read",
      "Deletes every backup",
      "Makes every website genuine",
      "Creates a public password"
    ],
    "options_en": [
      "Transforms readable information into protected form that needs a key to read",
      "Deletes every backup",
      "Makes every website genuine",
      "Creates a public password"
    ],
    "options_hi": [
      "पठनीय जानकारी को एक सुरक्षित गुप्त कोड (Ciphertext) में बदल देता है जिसे पढ़ने के लिए सही कुंजी (Key) चाहिए",
      "हर बैकअप को हटा देता है",
      "हर वेबसाइट को असली बनाता है",
      "एक सार्वजनिक पासवर्ड बनाता है"
    ],
    "answer": "Transforms readable information into protected form that needs a key to read",
    "correctAnswerIndex": 0,
    "explanation": "Encryption uses cryptographic algorithms to make plaintext unreadable without the decryption key.",
    "explanation_en": "Transforms readable information into protected form that needs a key to read.",
    "explanation_hi": "एन्क्रिप्शन सादे टेक्स्ट को एक अपठनीय कोड में बदल देता है जिसे केवल डिक्रिप्शन कुंजी वाला व्यक्ति ही पढ़ सकता है।"
  },
  {
    "id": "L4_T4_SCH_03",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "Why classify data as public, internal, or confidential?",
    "question_en": "Why classify data as public, internal, or confidential?",
    "question_hi": "डेटा को सार्वजनिक, आंतरिक या गोपनीय (Confidential) श्रेणियों में वर्गीकृत क्यों किया जाता है?",
    "options": [
      "To guide how it should be stored, accessed, and shared",
      "To make every file public",
      "To remove access controls",
      "To increase screen size"
    ],
    "options_en": [
      "To guide how it should be stored, accessed, and shared",
      "To make every file public",
      "To remove access controls",
      "To increase screen size"
    ],
    "options_hi": [
      "यह मार्गदर्शन करने के लिए कि डेटा को कैसे संग्रहीत, एक्सेस और सुरक्षित रूप से साझा किया जाना चाहिए",
      "हर फ़ाइल को सार्वजनिक करने के लिए",
      "एक्सेस नियंत्रण हटाने के लिए",
      "स्क्रीन का आकार बढ़ाने के लिए"
    ],
    "answer": "To guide how it should be stored, accessed, and shared",
    "correctAnswerIndex": 0,
    "explanation": "Data classification assigns security controls proportional to the sensitivity and value of the information.",
    "explanation_en": "To guide how it should be stored, accessed, and shared.",
    "explanation_hi": "वर्गीकरण से पता चलता है कि कौन सी फ़ाइल साधारण है और किसे कड़े पासवर्ड और एन्क्रिप्शन की आवश्यकता है।"
  },
  {
    "id": "L4_T4_SCH_04",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "What is a backup?",
    "question_en": "What is a backup?",
    "question_hi": "बैकअप (Backup) क्या है?",
    "options": [
      "A separate copy used to help restore information",
      "A type of phishing email",
      "A network cable",
      "A public password list"
    ],
    "options_en": [
      "A separate copy used to help restore information",
      "A type of phishing email",
      "A network cable",
      "A public password list"
    ],
    "options_hi": [
      "डेटा खो जाने पर उसे पुनर्स्थापित (Restore) करने में मदद के लिए रखी गई एक अलग अतिरिक्त प्रति",
      "फ़िशिंग ईमेल का एक प्रकार",
      "एक नेटवर्क केबल",
      "एक सार्वजनिक पासवर्ड सूची"
    ],
    "answer": "A separate copy used to help restore information",
    "correctAnswerIndex": 0,
    "explanation": "Backups duplicate critical data to secondary media so systems can recover from deletion or corruption.",
    "explanation_en": "A separate copy used to help restore information.",
    "explanation_hi": "बैकअप आपकी महत्वपूर्ण फ़ाइलों की एक सुरक्षित अतिरिक्त कॉपी होती है, जिससे मूल फ़ाइल नष्ट होने पर भी डेटा सुरक्षित रहता है।"
  },
  {
    "id": "L4_T4_SCH_05",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "Which file-sharing choice is safer for confidential data?",
    "question_en": "Which file-sharing choice is safer for confidential data?",
    "question_hi": "गोपनीय डेटा के लिए कौन सा फ़ाइल-शेयरिंग विकल्प अधिक सुरक्षित है?",
    "options": [
      "Give access only to intended, authorized recipients",
      "Use a public link with no restrictions",
      "Post it on social media",
      "Send it to an unknown address"
    ],
    "options_en": [
      "Give access only to intended, authorized recipients",
      "Use a public link with no restrictions",
      "Post it on social media",
      "Send it to an unknown address"
    ],
    "options_hi": [
      "केवल इच्छित और अधिकृत प्राप्तकर्ताओं को ही एक्सेस देना",
      "बिना किसी प्रतिबंध के सार्वजनिक लिंक का उपयोग करना",
      "इसे सोशल मीडिया पर पोस्ट करना",
      "इसे किसी अज्ञात पते पर भेजना"
    ],
    "answer": "Give access only to intended, authorized recipients",
    "correctAnswerIndex": 0,
    "explanation": "Restricted, authenticated access controls ensure only verified individuals can read or download files.",
    "explanation_en": "Give access only to intended, authorized recipients.",
    "explanation_hi": "गोपनीय फ़ाइल साझा करते समय हमेशा प्राप्तकर्ता का ईमेल सत्यापित करके केवल उसे ही अनुमति देनी चाहिए।"
  },
  {
    "id": "L4_T4_SCH_06",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "What does data minimization mean?",
    "question_en": "What does data minimization mean?",
    "question_hi": "डेटा मिनिमाइजेशन (Data Minimization) का क्या अर्थ है?",
    "options": [
      "Keeping or collecting only the information needed for a purpose",
      "Collecting every possible detail",
      "Sharing all records publicly",
      "Removing every backup"
    ],
    "options_en": [
      "Keeping or collecting only the information needed for a purpose",
      "Collecting every possible detail",
      "Sharing all records publicly",
      "Removing every backup"
    ],
    "options_hi": [
      "केवल वही जानकारी रखना या एकत्र करना जो किसी विशिष्ट उद्देश्य के लिए आवश्यक हो",
      "हर संभव विवरण एकत्र करना",
      "सभी रिकॉर्ड सार्वजनिक रूप से साझा करना",
      "हर बैकअप को हटाना"
    ],
    "answer": "Keeping or collecting only the information needed for a purpose",
    "correctAnswerIndex": 0,
    "explanation": "Collecting only essential data reduces exposure and organizational liability in the event of a breach.",
    "explanation_en": "Keeping or collecting only the information needed for a purpose.",
    "explanation_hi": "गैर-ज़रूरी व्यक्तिगत जानकारी इकट्ठा न करना डेटा मिनिमाइजेशन कहलाता है, जिससे डेटा लीक का खतरा कम होता है।"
  },
  {
    "id": "L4_T4_SCH_07",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "Why should backups be tested?",
    "question_en": "Why should backups be tested?",
    "question_hi": "बैकअप का समय-समय पर परीक्षण (Testing) क्यों किया जाना चाहिए?",
    "options": [
      "To check that data can actually be restored",
      "To make data public",
      "To disable passwords",
      "To make malware spread faster"
    ],
    "options_en": [
      "To check that data can actually be restored",
      "To make data public",
      "To disable passwords",
      "To make malware spread faster"
    ],
    "options_hi": [
      "यह पुष्टि करने के लिए कि आपातकाल में डेटा वास्तव में सफलतापूर्वक पुनर्स्थापित किया जा सकता है",
      "डेटा को सार्वजनिक करने के लिए",
      "पासवर्ड अक्षम करने के लिए",
      "मैलवेयर को तेज़ी से फैलाने के लिए"
    ],
    "answer": "To check that data can actually be restored",
    "correctAnswerIndex": 0,
    "explanation": "Unverified backups might be corrupt or incomplete, leading to total data loss during real disasters.",
    "explanation_en": "To check that data can actually be restored.",
    "explanation_hi": "परीक्षण के बिना यह नहीं जाना जा सकता कि बैकअप सही काम कर रहा है या नहीं; आपदा में खराब बैकअप किसी काम नहीं आता।"
  },
  {
    "id": "L4_T4_SCH_08",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "Which is an example of personal data?",
    "question_en": "Which is an example of personal data?",
    "question_hi": "व्यक्तिगत डेटा (Personal Data) का एक उदाहरण कौन सा है?",
    "options": [
      "A person's phone number linked to their identity",
      "A general maths formula",
      "A public weather forecast",
      "A common keyboard shortcut"
    ],
    "options_en": [
      "A person's phone number linked to their identity",
      "A general maths formula",
      "A public weather forecast",
      "A common keyboard shortcut"
    ],
    "options_hi": [
      "किसी व्यक्ति की पहचान से जुड़ा उसका निजी फ़ोन नंबर या आधार नंबर",
      "एक सामान्य गणितीय सूत्र",
      "सार्वजनिक मौसम का पूर्वानुमान",
      "एक सामान्य कीबोर्ड शॉर्टकट"
    ],
    "answer": "A person's phone number linked to their identity",
    "correctAnswerIndex": 0,
    "explanation": "Personally Identifiable Information (PII) relates directly to an identified living individual.",
    "explanation_en": "A person's phone number linked to their identity.",
    "explanation_hi": "फ़ोन नंबर, नाम, घर का पता और बायोमेट्रिक्स व्यक्तिगत डेटा हैं जिन्हें सुरक्षित रखना आवश्यक है।"
  },
  {
    "id": "L4_T4_SCH_09",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "What should you check before uploading a file to an online service?",
    "question_en": "What should you check before uploading a file to an online service?",
    "question_hi": "किसी ऑनलाइन सेवा पर फ़ाइल अपलोड करने से पहले आपको क्या जाँचना चाहिए?",
    "options": [
      "The service is approved and the sharing permissions are correct",
      "The file name is colourful",
      "The website has many advertisements",
      "The upload button is large"
    ],
    "options_en": [
      "The service is approved and the sharing permissions are correct",
      "The file name is colourful",
      "The website has many advertisements",
      "The upload button is large"
    ],
    "options_hi": [
      "कि सेवा स्कूल द्वारा स्वीकृत है और शेयरिंग अनुमतियाँ (Permissions) सही हैं",
      "फ़ाइल का नाम रंगीन है",
      "वेबसाइट पर कई विज्ञापन हैं",
      "अपलोड बटन बड़ा है"
    ],
    "answer": "The service is approved and the sharing permissions are correct",
    "correctAnswerIndex": 0,
    "explanation": "Verifying cloud provider vetting and permission scopes stops unintended public exposure of records.",
    "explanation_en": "The service is approved and the sharing permissions are correct.",
    "explanation_hi": "हमेशा जांचें कि क्लाउड सेवा विश्वसनीय है और फ़ाइल केवल सही लोगों के साथ ही शेयर की जा रही है।"
  },
  {
    "id": "L4_T4_SCH_10",
    "level": 4,
    "topic": "Data-Centric Architecture",
    "topicId": "data_centric_architecture",
    "mode": "school",
    "question": "Why should access to sensitive data be logged when appropriate?",
    "question_en": "Why should access to sensitive data be logged when appropriate?",
    "question_hi": "संवेदनशील डेटा तक पहुँच को उपयुक्त रूप से लॉग (रिकॉर्ड) क्यों किया जाना चाहिए?",
    "options": [
      "To help identify and investigate unusual access",
      "To display passwords publicly",
      "To replace encryption",
      "To guarantee no mistakes"
    ],
    "options_en": [
      "To help identify and investigate unusual access",
      "To display passwords publicly",
      "To replace encryption",
      "To guarantee no mistakes"
    ],
    "options_hi": [
      "असामान्य या अनधिकृत पहुँच की पहचान और जांच में मदद करने के लिए",
      "पासवर्ड सार्वजनिक रूप से प्रदर्शित करने के लिए",
      "एन्क्रिप्शन को बदलने के लिए",
      "कोई गलती न होने की गारंटी के लिए"
    ],
    "answer": "To help identify and investigate unusual access",
    "correctAnswerIndex": 0,
    "explanation": "Access logs provide non-repudiation and highlight anomalous exfiltration attempts.",
    "explanation_en": "To help identify and investigate unusual access.",
    "explanation_hi": "लॉग्स से पता चलता है कि किसने कब गोपनीय डेटा देखा, जिससे डेटा चोरी को पकड़ा जा सकता है।"
  },

  # Topic 20 (L4 T5): Infrastructure-Based Architecture
  {
    "id": "L4_T5_SCH_01",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "What is IT infrastructure?",
    "question_en": "What is IT infrastructure?",
    "question_hi": "IT इन्फ्रास्ट्रक्चर (IT Infrastructure) क्या है?",
    "options": [
      "The hardware, software, networks, and services supporting IT",
      "Only the classroom furniture",
      "A list of student birthdays",
      "A computer game's score"
    ],
    "options_en": [
      "The hardware, software, networks, and services supporting IT",
      "Only the classroom furniture",
      "A list of student birthdays",
      "A computer game's score"
    ],
    "options_hi": [
      "हार्डवेयर, सॉफ़्टवेयर, नेटवर्क और सेवाएं जो सूचना प्रौद्योगिकी को संचालित और समर्थन करती हैं",
      "केवल कक्षा का फर्नीचर",
      "छात्रों के जन्मदिन की सूची",
      "कंप्यूटर गेम का स्कोर"
    ],
    "answer": "The hardware, software, networks, and services supporting IT",
    "correctAnswerIndex": 0,
    "explanation": "IT infrastructure encompasses the collective physical and virtual systems powering computing services.",
    "explanation_en": "The hardware, software, networks, and services supporting IT.",
    "explanation_hi": "कंप्यूटर, सर्वर, केबल, राउटर और ऑपरेटिंग सिस्टम मिलकर IT इन्फ्रास्ट्रक्चर बनाते हैं।"
  },
  {
    "id": "L4_T5_SCH_02",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "What is a server?",
    "question_en": "What is a server?",
    "question_hi": "एक सर्वर (Server) क्या है?",
    "options": [
      "A system that provides services or resources to other devices",
      "A type of mouse pad",
      "A screen-cleaning cloth",
      "A phone ringtone"
    ],
    "options_en": [
      "A system that provides services or resources to other devices",
      "A type of mouse pad",
      "A screen-cleaning cloth",
      "A phone ringtone"
    ],
    "options_hi": [
      "एक ऐसा कंप्यूटर सिस्टम जो नेटवर्क पर अन्य उपकरणों को सेवाएं, डेटा या संसाधन प्रदान करता है",
      "माउस पैड का एक प्रकार",
      "स्क्रीन साफ करने का कपड़ा",
      "फ़ोन की रिंगटोन"
    ],
    "answer": "A system that provides services or resources to other devices",
    "correctAnswerIndex": 0,
    "explanation": "Servers host applications, databases, and websites, delivering resources to client machines over a network.",
    "explanation_en": "A system that provides services or resources to other devices.",
    "explanation_hi": "सर्वर एक शक्तिशाली कंप्यूटर होता है जो कई यूज़र्स को वेबसाइट, ईमेल या डेटाबेस सेवाएं प्रदान करता है।"
  },
  {
    "id": "L4_T5_SCH_03",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Why should access to a server room be restricted?",
    "question_en": "Why should access to a server room be restricted?",
    "question_hi": "सर्वर रूम तक भौतिक पहुँच (Physical Access) को प्रतिबंधित क्यों किया जाना चाहिए?",
    "options": [
      "To prevent unauthorized physical access or tampering",
      "To improve Wi-Fi colour",
      "To make passwords public",
      "To avoid all maintenance"
    ],
    "options_en": [
      "To prevent unauthorized physical access or tampering",
      "To improve Wi-Fi colour",
      "To make passwords public",
      "To avoid all maintenance"
    ],
    "options_hi": [
      "अनधिकृत भौतिक पहुँच, छेड़छाड़ या उपकरणों को नुकसान से रोकने के लिए",
      "वाई-फ़ाई का रंग बेहतर करने के लिए",
      "पासवर्ड सार्वजनिक करने के लिए",
      "सभी रखरखाव से बचने के लिए"
    ],
    "answer": "To prevent unauthorized physical access or tampering",
    "correctAnswerIndex": 0,
    "explanation": "Physical access to servers allows attackers to bypass software controls via direct console or drive extraction.",
    "explanation_en": "To prevent unauthorized physical access or tampering.",
    "explanation_hi": "यदि कोई सर्वर तक शारीरिक रूप से पहुँच जाए तो वह हार्ड ड्राइव निकाल सकता है या सीधे केबल जोड़कर हैक कर सकता है।"
  },
  {
    "id": "L4_T5_SCH_04",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "What is a security patch?",
    "question_en": "What is a security patch?",
    "question_hi": "एक सुरक्षा पैच (Security Patch) क्या है?",
    "options": [
      "An update that fixes a software weakness or problem",
      "A sticker on a laptop",
      "A spare keyboard key",
      "A type of social media post"
    ],
    "options_en": [
      "An update that fixes a software weakness or problem",
      "A sticker on a laptop",
      "A spare keyboard key",
      "A type of social media post"
    ],
    "options_hi": [
      "एक ऐसा सॉफ़्टवेयर अपडेट जो किसी ज्ञात सुरक्षा कमज़ोरी या बग को ठीक करता है",
      "लैपटॉप पर लगा एक स्टिकर",
      "एक अतिरिक्त कीबोर्ड कुंजी",
      "सोशल मीडिया पोस्ट का एक प्रकार"
    ],
    "answer": "An update that fixes a software weakness or problem",
    "correctAnswerIndex": 0,
    "explanation": "Security patches fix vulnerabilities in code before malicious actors can exploit them.",
    "explanation_en": "An update that fixes a software weakness or problem.",
    "explanation_hi": "सॉफ़्टवेयर बनाने वाली कंपनी जब कमज़ोरी ठीक करने के लिए कोड अपडेट जारी करती है, तो उसे सिक्योरिटी पैच कहते हैं।"
  },
  {
    "id": "L4_T5_SCH_05",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Why remove or disable unused services on a server?",
    "question_en": "Why remove or disable unused services on a server?",
    "question_hi": "सर्वर पर अप्रयुक्त सेवाओं (Unused Services) को हटाना या अक्षम करना क्यों आवश्यक है?",
    "options": [
      "They may create unnecessary ways for attackers to access it",
      "They always improve graphics",
      "They make all files public",
      "They stop the need for backups"
    ],
    "options_en": [
      "They may create unnecessary ways for attackers to access it",
      "They always improve graphics",
      "They make all files public",
      "They stop the need for backups"
    ],
    "options_hi": [
      "वे हमलावरों के लिए सर्वर में सेंध लगाने के अनावश्यक रास्ते (Attack Surface) बना सकती हैं",
      "वे हमेशा ग्राफिक्स में सुधार करती हैं",
      "वे सभी फ़ाइलों को सार्वजनिक करती हैं",
      "वे बैकअप की आवश्यकता को समाप्त करती हैं"
    ],
    "answer": "They may create unnecessary ways for attackers to access it",
    "correctAnswerIndex": 0,
    "explanation": "Server hardening requires shutting down unneeded ports and background daemons to minimize exposure.",
    "explanation_en": "They may create unnecessary ways for attackers to access it.",
    "explanation_hi": "फ़ालतू सेवाओं को बंद करने से हैकर्स के लिए कमज़ोरियां ढूंढने का अवसर बहुत कम हो जाता है।"
  },
  {
    "id": "L4_T5_SCH_06",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Why keep records of important infrastructure changes?",
    "question_en": "Why keep records of important infrastructure changes?",
    "question_hi": "इन्फ्रास्ट्रक्चर में किए गए महत्वपूर्ण परिवर्तनों का रिकॉर्ड (Change Log) क्यों रखना चाहिए?",
    "options": [
      "To track changes and help investigate problems",
      "To share passwords with everyone",
      "To remove access controls",
      "To stop system updates"
    ],
    "options_en": [
      "To track changes and help investigate problems",
      "To share passwords with everyone",
      "To remove access controls",
      "To stop system updates"
    ],
    "options_hi": [
      "बदलावों पर नज़र रखने और समस्या आने पर कारण का पता लगाने में मदद के लिए",
      "सभी के साथ पासवर्ड साझा करने के लिए",
      "एक्सेस नियंत्रण हटाने के लिए",
      "सिस्टम अपडेट रोकने के लिए"
    ],
    "answer": "To track changes and help investigate problems",
    "correctAnswerIndex": 0,
    "explanation": "Change management tracking simplifies root cause analysis during outages or configuration missteps.",
    "explanation_en": "To track changes and help investigate problems.",
    "explanation_hi": "रिकॉर्ड रहने से अगर सर्वर में कोई खराबी आती है तो तुरंत पता चल जाता है कि हाल ही में क्या बदलाव किया गया था।"
  },
  {
    "id": "L4_T5_SCH_07",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Which is an example of physical security for IT infrastructure?",
    "question_en": "Which is an example of physical security for IT infrastructure?",
    "question_hi": "IT इन्फ्रास्ट्रक्चर के लिए भौतिक सुरक्षा (Physical Security) का एक उदाहरण कौन सा है?",
    "options": [
      "A locked server room with controlled access",
      "A public password poster",
      "An unknown USB drive",
      "An open administrator account"
    ],
    "options_en": [
      "A locked server room with controlled access",
      "A public password poster",
      "An unknown USB drive",
      "An open administrator account"
    ],
    "options_hi": [
      "नियंत्रित बायोमेट्रिक या कार्ड एक्सेस वाला एक ताला लगा सर्वर रूम",
      "एक सार्वजनिक पासवर्ड पोस्टर",
      "एक अज्ञात USB ड्राइव",
      "एक खुला व्यवस्थापक खाता"
    ],
    "answer": "A locked server room with controlled access",
    "correctAnswerIndex": 0,
    "explanation": "Physical security controls like badge readers, locks, and CCTV defend core server hardware.",
    "explanation_en": "A locked server room with controlled access.",
    "explanation_hi": "सर्वर रूम में ताला लगाना और केवल अधिकृत कर्मचारियों को ही अंदर जाने देना भौतिक सुरक्षा का मुख्य उपाय है।"
  },
  {
    "id": "L4_T5_SCH_08",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Why should critical systems have a recovery plan?",
    "question_en": "Why should critical systems have a recovery plan?",
    "question_hi": "महत्वपूर्ण प्रणालियों के लिए आपदा पुनर्प्राप्ति योजना (Disaster Recovery Plan) क्यों होनी चाहिए?",
    "options": [
      "To restore important services after a failure or incident",
      "To ensure nobody can use them",
      "To publish private data",
      "To remove all monitoring"
    ],
    "options_en": [
      "To restore important services after a failure or incident",
      "To ensure nobody can use them",
      "To publish private data",
      "To remove all monitoring"
    ],
    "options_hi": [
      "किसी खराबी, आपदा या साइबर हमले के बाद आवश्यक सेवाओं को शीघ्रता से बहाल करने के लिए",
      "यह सुनिश्चित करने के लिए कि कोई उनका उपयोग न कर सके",
      "निजी डेटा प्रकाशित करने के लिए",
      "सभी निगरानी हटाने के लिए"
    ],
    "answer": "To restore important services after a failure or incident",
    "correctAnswerIndex": 0,
    "explanation": "Disaster recovery plans define steps to bring offline infrastructure back into production safely.",
    "explanation_en": "To restore important services after a failure or incident.",
    "explanation_hi": "योजना होने से सर्वर क्रैश या आग लगने पर भी स्कूल का काम बिना रुकावट तुरंत दोबारा शुरू किया जा सकता है।"
  },
  {
    "id": "L4_T5_SCH_09",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "What should be done with a server account that is no longer needed?",
    "question_en": "What should be done with a server account that is no longer needed?",
    "question_hi": "ऐसे सर्वर खाते का क्या किया जाना चाहिए जिसकी अब आवश्यकता नहीं है?",
    "options": [
      "Disable or remove it according to policy",
      "Share it publicly",
      "Keep it active forever",
      "Use it for every person"
    ],
    "options_en": [
      "Disable or remove it according to policy",
      "Share it publicly",
      "Keep it active forever",
      "Use it for every person"
    ],
    "options_hi": [
      "सुरक्षा नीति के अनुसार उसे तुरंत अक्षम (Disable) या हटा देना चाहिए",
      "इसे सार्वजनिक रूप से साझा करें",
      "इसे हमेशा के लिए सक्रिय रखें",
      "हर व्यक्ति के लिए इसका इस्तेमाल करें"
    ],
    "answer": "Disable or remove it according to policy",
    "correctAnswerIndex": 0,
    "explanation": "Stale accounts represent unmonitored backdoors that adversaries exploit if left active.",
    "explanation_en": "Disable or remove it according to policy.",
    "explanation_hi": "पुराने अप्रयुक्त खातों को बंद करना आवश्यक है ताकि कोई हैकर चुपके से उनका इस्तेमाल न कर सके।"
  },
  {
    "id": "L4_T5_SCH_10",
    "level": 4,
    "topic": "Infrastructure-Based Architecture",
    "topicId": "infrastructure_based_architecture",
    "mode": "school",
    "question": "Why is infrastructure monitoring important?",
    "question_en": "Why is infrastructure monitoring important?",
    "question_hi": "इन्फ्रास्ट्रक्चर की निरंतर निगरानी (Infrastructure Monitoring) क्यों महत्वपूर्ण है?",
    "options": [
      "It can help identify outages, unusual activity, and performance problems",
      "It guarantees no attack can occur",
      "It makes all users administrators",
      "It replaces security updates"
    ],
    "options_en": [
      "It can help identify outages, unusual activity, and performance problems",
      "It guarantees no attack can occur",
      "It makes all users administrators",
      "It replaces security updates"
    ],
    "options_hi": [
      "यह सिस्टम रुकावटों (Outages), असामान्य गतिविधि और प्रदर्शन समस्याओं की तुरंत पहचान करने में मदद करती है",
      "यह गारंटी देती है कि कोई हमला नहीं हो सकता",
      "यह सभी उपयोगकर्ताओं को व्यवस्थापक बनाती है",
      "यह सुरक्षा अपडेट की जगह लेती है"
    ],
    "answer": "It can help identify outages, unusual activity, and performance problems",
    "correctAnswerIndex": 0,
    "explanation": "Health and security telemetry alerts administrators to hardware bottlenecks and anomalous traffic patterns.",
    "explanation_en": "It can help identify outages, unusual activity, and performance problems.",
    "explanation_hi": "निगरानी से पता चलता है कि सर्वर सुचारू चल रहा है या कहीं कोई खराबी या साइबर हमला तो नहीं हो रहा।"
  }
]

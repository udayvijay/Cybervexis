# -*- coding: utf-8 -*-
"""Level 2: Firewalls (5 topics x 10 questions = 50 questions)"""

level2_questions = [
  # Topic 6 (L2 T1): Packet Filtering Firewall
  {
    "id": "L2_T1_SCH_01",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "What information may a basic packet-filtering firewall use to make a decision?",
    "question_en": "What information may a basic packet-filtering firewall use to make a decision?",
    "question_hi": "एक बुनियादी पैकेट-फ़िल्टरिंग फ़ायरवॉल निर्णय लेने के लिए किस जानकारी का उपयोग कर सकता है?",
    "options": [
      "Source/destination addresses, ports, and protocol",
      "The user's favourite colour",
      "The monitor size",
      "The keyboard language"
    ],
    "options_en": [
      "Source/destination addresses, ports, and protocol",
      "The user's favourite colour",
      "The monitor size",
      "The keyboard language"
    ],
    "options_hi": [
      "स्रोत/गंतव्य IP पते, पोर्ट (Ports) और प्रोटोकॉल (Protocol)",
      "उपयोगकर्ता का पसंदीदा रंग",
      "मॉनिटर का आकार",
      "कीबोर्ड की भाषा"
    ],
    "answer": "Source/destination addresses, ports, and protocol",
    "correctAnswerIndex": 0,
    "explanation": "Packet-filtering firewalls inspect headers such as IP addresses, port numbers, and protocols to allow or block traffic.",
    "explanation_en": "Packet-filtering firewalls inspect headers such as IP addresses, port numbers, and protocols to allow or block traffic.",
    "explanation_hi": "पैकेट फ़िल्टरिंग फ़ायरवॉल नेटवर्क ट्रैफ़िक के IP पते, पोर्ट और प्रोटोकॉल की जांच करके यह तय करता है कि उसे जाने देना है या रोकना है।"
  },
  {
    "id": "L2_T1_SCH_02",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "What is the main job of a packet-filtering firewall?",
    "question_en": "What is the main job of a packet-filtering firewall?",
    "question_hi": "पैकेट-फ़िल्टरिंग फ़ायरवॉल का मुख्य कार्य क्या है?",
    "options": [
      "Allow or block network packets using rules",
      "Write essays",
      "Charge a laptop",
      "Create passwords for every user"
    ],
    "options_en": [
      "Allow or block network packets using rules",
      "Write essays",
      "Charge a laptop",
      "Create passwords for every user"
    ],
    "options_hi": [
      "सुरक्षा नियमों के आधार पर नेटवर्क पैकेट को अनुमति देना या ब्लॉक करना",
      "निबंध लिखना",
      "लैपटॉप चार्ज करना",
      "प्रत्येक उपयोगकर्ता के लिए पासवर्ड बनाना"
    ],
    "answer": "Allow or block network packets using rules",
    "correctAnswerIndex": 0,
    "explanation": "The primary role is filtering inbound and outbound packets according to predefined security rules.",
    "explanation_en": "The primary role is filtering inbound and outbound packets according to predefined security rules.",
    "explanation_hi": "इसका मुख्य काम तय नियमों के अनुसार आने-जाने वाले डेटा पैकेट्स को फिल्टर करना है।"
  },
  {
    "id": "L2_T1_SCH_03",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "A firewall rule blocks incoming traffic on an unused port. What is the likely benefit?",
    "question_en": "A firewall rule blocks incoming traffic on an unused port. What is the likely benefit?",
    "question_hi": "एक फ़ायरवॉल नियम अप्रयुक्त पोर्ट पर आने वाले ट्रैफ़िक को ब्लॉक करता है। इसका संभावित लाभ क्या है?",
    "options": [
      "It reduces unnecessary network access",
      "It makes all files public",
      "It disables backups",
      "It guarantees no attack can happen"
    ],
    "options_en": [
      "It reduces unnecessary network access",
      "It makes all files public",
      "It disables backups",
      "It guarantees no attack can happen"
    ],
    "options_hi": [
      "यह अनावश्यक नेटवर्क पहुँच और संभावित हमलों के रास्ते को कम करता है",
      "यह सभी फ़ाइलों को सार्वजनिक कर देता है",
      "यह बैकअप को अक्षम कर देता है",
      "यह गारंटी देता है कि कोई हमला नहीं हो सकता"
    ],
    "answer": "It reduces unnecessary network access",
    "correctAnswerIndex": 0,
    "explanation": "Closing unused ports shrinks the attack surface and prevents unauthorized network discovery.",
    "explanation_en": "Closing unused ports shrinks the attack surface and prevents unauthorized network discovery.",
    "explanation_hi": "जिन पोर्ट्स का उपयोग नहीं हो रहा है उन्हें बंद करने से हैकर्स के लिए घुसपैठ का रास्ता बंद हो जाता है।"
  },
  {
    "id": "L2_T1_SCH_04",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "What does a network port help identify?",
    "question_en": "What does a network port help identify?",
    "question_hi": "एक नेटवर्क पोर्ट (Network Port) किसकी पहचान करने में मदद करता है?",
    "options": [
      "A service or application endpoint for network communication",
      "The physical size of a laptop",
      "A person's home address",
      "A printer's paper size"
    ],
    "options_en": [
      "A service or application endpoint for network communication",
      "The physical size of a laptop",
      "A person's home address",
      "A printer's paper size"
    ],
    "options_hi": [
      "नेटवर्क संचार के लिए किसी विशिष्ट सेवा या एप्लिकेशन का एंडपॉइंट (जैसे वेब या ईमेल)",
      "लैपटॉप का भौतिक आकार",
      "किसी व्यक्ति का घर का पता",
      "प्रिंटर के कागज़ का आकार"
    ],
    "answer": "A service or application endpoint for network communication",
    "correctAnswerIndex": 0,
    "explanation": "Ports identify specific application processes running on a device (e.g., port 80 for HTTP, 443 for HTTPS).",
    "explanation_en": "Ports identify specific application processes running on a device (e.g., port 80 for HTTP, 443 for HTTPS).",
    "explanation_hi": "नेटवर्क पोर्ट डिवाइस पर चलने वाले विशिष्ट एप्लिकेशन या सेवा (जैसे वेब या ईमेल) की पहचान करता है।"
  },
  {
    "id": "L2_T1_SCH_05",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "If a firewall blocks a legitimate school website by mistake, what should happen?",
    "question_en": "If a firewall blocks a legitimate school website by mistake, what should happen?",
    "question_hi": "यदि फ़ायरवॉल गलती से स्कूल की किसी वैध वेबसाइट को ब्लॉक कर देता है, तो क्या किया जाना चाहिए?",
    "options": [
      "An authorized administrator should review the rule",
      "Students should disable the firewall",
      "Everyone should share passwords",
      "The network should be abandoned"
    ],
    "options_en": [
      "An authorized administrator should review the rule",
      "Students should disable the firewall",
      "Everyone should share passwords",
      "The network should be abandoned"
    ],
    "options_hi": [
      "अधिकृत IT व्यवस्थापक (Administrator) को नियम की समीक्षा करनी चाहिए",
      "छात्रों को फ़ायरवॉल बंद कर देना चाहिए",
      "सभी को पासवर्ड साझा करना चाहिए",
      "नेटवर्क का उपयोग छोड़ देना चाहिए"
    ],
    "answer": "An authorized administrator should review the rule",
    "correctAnswerIndex": 0,
    "explanation": "Only authorized administrators should review and tune firewall rules to resolve false positives.",
    "explanation_en": "Only authorized administrators should review and tune firewall rules to resolve false positives.",
    "explanation_hi": "केवल अधिकृत IT एडमिन को ही फ़ायरवॉल नियमों की जांच करके सही वेबसाइट को अनुमति देनी चाहिए।"
  },
  {
    "id": "L2_T1_SCH_06",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "Which firewall rule is generally safer?",
    "question_en": "Which firewall rule is generally safer?",
    "question_hi": "कौन सा फ़ायरवॉल नियम आम तौर पर अधिक सुरक्षित माना जाता है?",
    "options": [
      "Allow everything from everywhere",
      "Allow only the traffic needed for approved services",
      "Disable all logging",
      "Use unknown rules copied online"
    ],
    "options_en": [
      "Allow everything from everywhere",
      "Allow only the traffic needed for approved services",
      "Disable all logging",
      "Use unknown rules copied online"
    ],
    "options_hi": [
      "हर जगह से सब कुछ अनुमति देना",
      "केवल स्वीकृत सेवाओं के लिए आवश्यक ट्रैफ़िक को ही अनुमति देना",
      "सभी लॉगिंग अक्षम करना",
      "इंटरनेट से कॉपी किए गए अज्ञात नियमों का उपयोग करना"
    ],
    "answer": "Allow only the traffic needed for approved services",
    "correctAnswerIndex": 1,
    "explanation": "Default-deny policy allows only necessary approved traffic, maintaining highest security posture.",
    "explanation_en": "Default-deny policy allows only necessary approved traffic, maintaining highest security posture.",
    "explanation_hi": "सुरक्षा के लिए केवल आवश्यक सेवाओं को अनुमति देकर बाकी सभी अनचाहे ट्रैफ़िक को ब्लॉक करना सबसे सुरक्षित नीति है।"
  },
  {
    "id": "L2_T1_SCH_07",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "Can packet filtering inspect every detail of an encrypted webpage's contents?",
    "question_en": "Can packet filtering inspect every detail of an encrypted webpage's contents?",
    "question_hi": "क्या बुनियादी पैकेट फ़िल्टरिंग किसी एन्क्रिप्टेड वेबपेज की आंतरिक सामग्री के हर विवरण का निरीक्षण कर सकती है?",
    "options": [
      "Yes, automatically in every case",
      "No, basic packet filtering usually uses packet headers and rules",
      "Only when the computer is off",
      "Only on paper"
    ],
    "options_en": [
      "Yes, automatically in every case",
      "No, basic packet filtering usually uses packet headers and rules",
      "Only when the computer is off",
      "Only on paper"
    ],
    "options_hi": [
      "हाँ, हर मामले में स्वचालित रूप से",
      "नहीं, बुनियादी पैकेट फ़िल्टरिंग आमतौर पर केवल पैकेट हेडर और नियमों की जाँच करती है",
      "केवल तब जब कंप्यूटर बंद हो",
      "केवल कागज़ पर"
    ],
    "answer": "No, basic packet filtering usually uses packet headers and rules",
    "correctAnswerIndex": 1,
    "explanation": "Packet-filtering operates at Layer 3/4 headers and cannot inspect encrypted Layer 7 payload contents.",
    "explanation_en": "Packet-filtering operates at Layer 3/4 headers and cannot inspect encrypted Layer 7 payload contents.",
    "explanation_hi": "बुनियादी पैकेट फ़िल्टरिंग केवल पैकेट के पते और पोर्ट की जांच करती है, एन्क्रिप्टेड डेटा के भीतर का पाठ नहीं पढ़ सकती।"
  },
  {
    "id": "L2_T1_SCH_08",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "Why should firewall rules be documented?",
    "question_en": "Why should firewall rules be documented?",
    "question_hi": "फ़ायरवॉल नियमों का लिखित दस्तावेज़ीकरण (Documentation) क्यों किया जाना चाहिए?",
    "options": [
      "To understand why traffic is allowed or blocked",
      "To make passwords visible",
      "To increase screen brightness",
      "To avoid updates forever"
    ],
    "options_en": [
      "To understand why traffic is allowed or blocked",
      "To make passwords visible",
      "To increase screen brightness",
      "To avoid updates forever"
    ],
    "options_hi": [
      "यह समझने के लिए कि ट्रैफ़िक को क्यों अनुमति दी गई है या ब्लॉक किया गया है",
      "पासवर्ड को सभी के लिए दृश्यमान बनाने के लिए",
      "स्क्रीन की चमक बढ़ाने के लिए",
      "हमेशा के लिए अपडेट से बचने के लिए"
    ],
    "answer": "To understand why traffic is allowed or blocked",
    "correctAnswerIndex": 0,
    "explanation": "Rule documentation helps administrators audit network security policies and debug configuration errors.",
    "explanation_en": "Rule documentation helps administrators audit network security policies and debug configuration errors.",
    "explanation_hi": "नियमों का रिकॉर्ड रखने से व्यवस्थापकों को यह पता रहता है कि कौन सा नियम किस उद्देश्य से बनाया गया है।"
  },
  {
    "id": "L2_T1_SCH_09",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "What could happen if a firewall rule is too permissive?",
    "question_en": "What could happen if a firewall rule is too permissive?",
    "question_hi": "यदि कोई फ़ायरवॉल नियम अत्यधिक ढीला (too permissive) हो तो क्या हो सकता है?",
    "options": [
      "Unwanted traffic may reach a system",
      "The screen becomes smaller",
      "Files automatically print",
      "The keyboard stops typing"
    ],
    "options_en": [
      "Unwanted traffic may reach a system",
      "The screen becomes smaller",
      "Files automatically print",
      "The keyboard stops typing"
    ],
    "options_hi": [
      "अवांछित या दुर्भावनापूर्ण ट्रैफ़िक सिस्टम तक पहुँच सकता है",
      "स्क्रीन छोटी हो जाती है",
      "फ़ाइलें अपने आप प्रिंट होने लगती हैं",
      "कीबोर्ड टाइप करना बंद कर देता है"
    ],
    "answer": "Unwanted traffic may reach a system",
    "correctAnswerIndex": 0,
    "explanation": "Overly permissive rules create vulnerabilities by permitting unauthorized connections into the network.",
    "explanation_en": "Overly permissive rules create vulnerabilities by permitting unauthorized connections into the network.",
    "explanation_hi": "ढीले नियमों के कारण हैकर या दुर्भावनापूर्ण ट्रैफ़िक आसानी से नेटवर्क के अंदर प्रवेश कर सकते हैं।"
  },
  {
    "id": "L2_T1_SCH_10",
    "level": 2,
    "topic": "Packet Filtering Firewall",
    "topicId": "packet_filtering_firewall",
    "mode": "school",
    "question": "Who should change firewall settings on a school network?",
    "question_en": "Who should change firewall settings on a school network?",
    "question_hi": "स्कूल के नेटवर्क पर फ़ायरवॉल सेटिंग्स में बदलाव किसे करना चाहिए?",
    "options": [
      "Any visitor",
      "An authorized IT administrator",
      "A random online user",
      "Anyone who sees an alert"
    ],
    "options_en": [
      "Any visitor",
      "An authorized IT administrator",
      "A random online user",
      "Anyone who sees an alert"
    ],
    "options_hi": [
      "कोई भी आगंतुक",
      "एक अधिकृत IT व्यवस्थापक (Administrator)",
      "कोई भी यादृच्छिक ऑनलाइन उपयोगकर्ता",
      "कोई भी व्यक्ति जो चेतावनी देखता है"
    ],
    "answer": "An authorized IT administrator",
    "correctAnswerIndex": 1,
    "explanation": "Only trained IT personnel with delegated permissions should manage infrastructure firewalls.",
    "explanation_en": "Only trained IT personnel with delegated permissions should manage infrastructure firewalls.",
    "explanation_hi": "फ़ायरवॉल पूरे स्कूल नेटवर्क की सुरक्षा करता है, इसलिए केवल प्रशिक्षित IT प्रशासक ही इसमें बदलाव कर सकते हैं।"
  },

  # Topic 7 (L2 T2): Stateful Inspection Firewall
  {
    "id": "L2_T2_SCH_01",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "What extra information does a stateful firewall track compared with a basic stateless filter?",
    "question_en": "What extra information does a stateful firewall track compared with a basic stateless filter?",
    "question_hi": "एक स्टेटफ़ुल फ़ायरवॉल बुनियादी स्टेटलेस फ़िल्टर की तुलना में कौन सी अतिरिक्त जानकारी ट्रैक करता है?",
    "options": [
      "The state of active connections",
      "The user's age",
      "The colour of a website",
      "The battery percentage"
    ],
    "options_en": [
      "The state of active connections",
      "The user's age",
      "The colour of a website",
      "The battery percentage"
    ],
    "options_hi": [
      "सक्रिय कनेक्शनों की स्थिति (State of active connections)",
      "उपयोगकर्ता की आयु",
      "वेबसाइट का रंग",
      "बैटरी का प्रतिशत"
    ],
    "answer": "The state of active connections",
    "correctAnswerIndex": 0,
    "explanation": "Stateful firewalls maintain a state table tracking the context and status of established sessions.",
    "explanation_en": "Stateful firewalls maintain a state table tracking the context and status of established sessions.",
    "explanation_hi": "स्टेटफ़ुल फ़ायरवॉल नेटवर्क कनेक्शन के आरंभ से अंत तक की पूरी स्थिति (State) का रिकॉर्ड रखता है।"
  },
  {
    "id": "L2_T2_SCH_02",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "A reply packet arrives as part of an allowed connection. What can a stateful firewall do?",
    "question_en": "A reply packet arrives as part of an allowed connection. What can a stateful firewall do?",
    "question_hi": "एक उत्तर पैकेट पहले से स्वीकृत कनेक्शन के हिस्से के रूप में आता है। एक स्टेटफ़ुल फ़ायरवॉल क्या कर सकता है?",
    "options": [
      "Recognize it as related to the tracked connection",
      "Always treat it as a new computer",
      "Delete all network rules",
      "Change the user's password"
    ],
    "options_en": [
      "Recognize it as related to the tracked connection",
      "Always treat it as a new computer",
      "Delete all network rules",
      "Change the user's password"
    ],
    "options_hi": [
      "इसे ट्रैक किए गए मौजूदा कनेक्शन से संबंधित पहचानकर स्वतः आने की अनुमति देना",
      "इसे हमेशा एक नए कंप्यूटर के रूप में मानना",
      "सभी नेटवर्क नियमों को हटा देना",
      "उपयोगकर्ता का पासवर्ड बदल देना"
    ],
    "answer": "Recognize it as related to the tracked connection",
    "correctAnswerIndex": 0,
    "explanation": "Stateful firewalls automatically allow established return traffic by referencing their connection table.",
    "explanation_en": "Stateful firewalls automatically allow established return traffic by referencing their connection table.",
    "explanation_hi": "स्टेटफ़ुल फ़ायरवॉल यह याद रखता है कि आपने कौन सा अनुरोध भेजा था और उसका जवाब आने पर उसे आने देता है।"
  },
  {
    "id": "L2_T2_SCH_03",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Why can state tracking improve firewall decisions?",
    "question_en": "Why can state tracking improve firewall decisions?",
    "question_hi": "कनेक्शन स्टेट ट्रैकिंग फ़ायरवॉल के निर्णयों को बेहतर क्यों बनाती है?",
    "options": [
      "It helps distinguish expected connection traffic from unexpected traffic",
      "It removes the need for any rules",
      "It prevents all phishing",
      "It speeds up typing"
    ],
    "options_en": [
      "It helps distinguish expected connection traffic from unexpected traffic",
      "It removes the need for any rules",
      "It prevents all phishing",
      "It speeds up typing"
    ],
    "options_hi": [
      "यह अपेक्षित वैध ट्रैफ़िक को अप्रत्याशित या अनचाहे ट्रैफ़िक से अलग पहचानने में मदद करता है",
      "यह किसी भी नियम की आवश्यकता को समाप्त कर देता है",
      "यह सभी प्रकार की फ़िशिंग को रोकता है",
      "यह टाइपिंग को तेज़ करता है"
    ],
    "answer": "It helps distinguish expected connection traffic from unexpected traffic",
    "correctAnswerIndex": 0,
    "explanation": "Contextual session awareness blocks unsolicited incoming packets pretending to be responses.",
    "explanation_en": "Contextual session awareness blocks unsolicited incoming packets pretending to be responses.",
    "explanation_hi": "यह सुनिश्चित करता है कि केवल वही पैकेट अंदर आएं जिन्हें अंदर के सिस्टम ने स्वयं मंगाया हो।"
  },
  {
    "id": "L2_T2_SCH_04",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Does stateful inspection mean a firewall can understand every user's intention?",
    "question_en": "Does stateful inspection mean a firewall can understand every user's intention?",
    "question_hi": "क्या स्टेटफ़ुल इंस्पेक्शन का अर्थ यह है कि फ़ायरवॉल उपयोगकर्ता के हर इरादे को समझ सकता है?",
    "options": [
      "Yes",
      "No, it tracks connection information, not human intentions",
      "Only on weekends",
      "Only when offline"
    ],
    "options_en": [
      "Yes",
      "No, it tracks connection information, not human intentions",
      "Only on weekends",
      "Only when offline"
    ],
    "options_hi": [
      "हाँ",
      "नहीं, यह तकनीकी कनेक्शन जानकारी ट्रैक करता है, मानवीय इरादों को नहीं",
      "केवल सप्ताहांत पर",
      "केवल जब ऑफ़लाइन हो"
    ],
    "answer": "No, it tracks connection information, not human intentions",
    "correctAnswerIndex": 1,
    "explanation": "Stateful firewalls monitor protocol state flags and sockets, not human cognitive reasoning.",
    "explanation_en": "Stateful firewalls monitor protocol state flags and sockets, not human cognitive reasoning.",
    "explanation_hi": "फ़ायरवॉल केवल तकनीकी डेटा पैकेट और प्रोटोकॉल ट्रैक करता है, इंसान के मन की बात नहीं समझ सकता।"
  },
  {
    "id": "L2_T2_SCH_05",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Which is a good reason to review stateful firewall logs?",
    "question_en": "Which is a good reason to review stateful firewall logs?",
    "question_hi": "स्टेटफ़ुल फ़ायरवॉल लॉग्स की समीक्षा करने का एक अच्छा कारण क्या है?",
    "options": [
      "To investigate unusual or blocked connections",
      "To collect everyone's passwords",
      "To make a game run faster",
      "To remove all security controls"
    ],
    "options_en": [
      "To investigate unusual or blocked connections",
      "To collect everyone's passwords",
      "To make a game run faster",
      "To remove all security controls"
    ],
    "options_hi": [
      "असामान्य या ब्लॉक किए गए कनेक्शनों और संदिग्ध गतिविधियों की जांच करना",
      "सभी के पासवर्ड एकत्र करना",
      "गेम को तेज़ चलाना",
      "सभी सुरक्षा नियंत्रणों को हटाना"
    ],
    "answer": "To investigate unusual or blocked connections",
    "correctAnswerIndex": 0,
    "explanation": "Log analysis reveals port scanning, abnormal session spikes, and malicious connection attempts.",
    "explanation_en": "Log analysis reveals port scanning, abnormal session spikes, and malicious connection attempts.",
    "explanation_hi": "फ़ायरवॉल लॉग्स की जांच से पता चलता है कि नेटवर्क पर कोई असामान्य या अनधिकृत हमला तो नहीं हो रहा।"
  },
  {
    "id": "L2_T2_SCH_06",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "What may a stateful firewall do with an unexpected packet that does not match a valid connection?",
    "question_en": "What may a stateful firewall do with an unexpected packet that does not match a valid connection?",
    "question_hi": "एक स्टेटफ़ुल फ़ायरवॉल किसी ऐसे अप्रत्याशित पैकेट के साथ क्या करेगा जो किसी वैध कनेक्शन से मेल नहीं खाता?",
    "options": [
      "Block it according to its rules",
      "Automatically trust it",
      "Publish it online",
      "Turn it into a backup"
    ],
    "options_en": [
      "Block it according to its rules",
      "Automatically trust it",
      "Publish it online",
      "Turn it into a backup"
    ],
    "options_hi": [
      "अपने सुरक्षा नियमों के अनुसार उसे तुरंत ब्लॉक कर देगा",
      "स्वचालित रूप से उस पर भरोसा करेगा",
      "इसे ऑनलाइन प्रकाशित कर देगा",
      "इसे बैकअप में बदल देगा"
    ],
    "answer": "Block it according to its rules",
    "correctAnswerIndex": 0,
    "explanation": "Packets not belonging to an open, known session are dropped as potential unsolicited intrusion attempts.",
    "explanation_en": "Packets not belonging to an open, known session are dropped as potential unsolicited intrusion attempts.",
    "explanation_hi": "बिना किसी स्थापित सत्र के आने वाले अनजान पैकेट को फ़ायरवॉल संदिग्ध मानकर ब्लॉक कर देता है।"
  },
  {
    "id": "L2_T2_SCH_07",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Which statement is true?",
    "question_en": "Which statement is true?",
    "question_hi": "इनमें से कौन सा कथन सत्य है?",
    "options": [
      "Stateful firewalls track connection state",
      "Stateful firewalls are only used to clean screens",
      "They replace every security tool",
      "They make every website genuine"
    ],
    "options_en": [
      "Stateful firewalls track connection state",
      "Stateful firewalls are only used to clean screens",
      "They replace every security tool",
      "They make every website genuine"
    ],
    "options_hi": [
      "स्टेटफ़ुल फ़ायरवॉल कनेक्शन की स्थिति (State) को ट्रैक करते हैं",
      "स्टेटफ़ुल फ़ायरवॉल का उपयोग केवल स्क्रीन साफ़ करने के लिए किया जाता है",
      "वे हर सुरक्षा टूल की जगह लेते हैं",
      "वे हर वेबसाइट को असली बना देते हैं"
    ],
    "answer": "Stateful firewalls track connection state",
    "correctAnswerIndex": 0,
    "explanation": "Stateful firewalls track the full lifecycle of network sessions across TCP/UDP protocols.",
    "explanation_en": "Stateful firewalls track the full lifecycle of network sessions across TCP/UDP protocols.",
    "explanation_hi": "स्टेटफ़ुल फ़ायरवॉल की सबसे प्रमुख विशेषता यह है कि वे नेटवर्क कनेक्शन की स्थिति को ट्रैक करते हैं।"
  },
  {
    "id": "L2_T2_SCH_08",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Why are established connection rules useful?",
    "question_en": "Why are established connection rules useful?",
    "question_hi": "स्थापित कनेक्शन नियम (Established connection rules) क्यों उपयोगी होते हैं?",
    "options": [
      "They help permit legitimate replies while controlling new connections",
      "They reveal every user's password",
      "They make Wi-Fi public",
      "They stop all human error"
    ],
    "options_en": [
      "They help permit legitimate replies while controlling new connections",
      "They reveal every user's password",
      "They make Wi-Fi public",
      "They stop all human error"
    ],
    "options_hi": [
      "वे नए कनेक्शनों को नियंत्रित करते हुए वैध उत्तरों को नेटवर्क में आने की अनुमति देते हैं",
      "वे हर उपयोगकर्ता का पासवर्ड उजागर करते हैं",
      "वे वाई-फ़ाई को सार्वजनिक करते हैं",
      "वे सभी मानवीय त्रुटियों को रोकते हैं"
    ],
    "answer": "They help permit legitimate replies while controlling new connections",
    "correctAnswerIndex": 0,
    "explanation": "Established rules enable bi-directional traffic for authorized outbound requests without opening inbound ports.",
    "explanation_en": "Established rules enable bi-directional traffic for authorized outbound requests without opening inbound ports.",
    "explanation_hi": "यह नियम सुनिश्चित करते हैं कि बाहर भेजे गए अनुरोध का जवाब आसानी से आ सके और कोई अज्ञात व्यक्ति अंदर न घुस सके।"
  },
  {
    "id": "L2_T2_SCH_09",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "What should an administrator do if a firewall blocks an expected application?",
    "question_en": "What should an administrator do if a firewall blocks an expected application?",
    "question_hi": "यदि फ़ायरवॉल किसी आवश्यक स्कूल एप्लिकेशन को ब्लॉक कर देता है, तो व्यवस्थापक को क्या करना चाहिए?",
    "options": [
      "Check logs and rules before making a controlled change",
      "Turn off all security permanently",
      "Share the admin password",
      "Ignore the problem forever"
    ],
    "options_en": [
      "Check logs and rules before making a controlled change",
      "Turn off all security permanently",
      "Share the admin password",
      "Ignore the problem forever"
    ],
    "options_hi": [
      "नियंत्रित परिवर्तन करने से पहले लॉग और नियमों की जांच करें",
      "सभी सुरक्षा को स्थायी रूप से बंद कर दें",
      "व्यवस्थापक पासवर्ड साझा करें",
      "समस्या को हमेशा के लिए अनदेखा करें"
    ],
    "answer": "Check logs and rules before making a controlled change",
    "correctAnswerIndex": 0,
    "explanation": "Diagnosing block logs pinpoint the precise port/protocol needed, avoiding broad unsafe rule changes.",
    "explanation_en": "Diagnosing block logs pinpoint the precise port/protocol needed, avoiding broad unsafe rule changes.",
    "explanation_hi": "व्यवस्थापक को पहले लॉग्स देखकर जांच करनी चाहिए कि कौन सा पोर्ट ब्लॉक हुआ है और फिर सावधानी से नियम बदलना चाहिए।"
  },
  {
    "id": "L2_T2_SCH_10",
    "level": 2,
    "topic": "Stateful Inspection Firewall",
    "topicId": "stateful_inspection_firewall",
    "mode": "school",
    "question": "Can a stateful firewall still need updates and correct configuration?",
    "question_en": "Can a stateful firewall still need updates and correct configuration?",
    "question_hi": "क्या एक स्टेटफ़ुल फ़ायरवॉल को भी नियमित अपडेट और सही कॉन्फ़िगरेशन की आवश्यकता होती है?",
    "options": [
      "Yes",
      "No, it never needs maintenance",
      "Only if the monitor breaks",
      "Only on school holidays"
    ],
    "options_en": [
      "Yes",
      "No, it never needs maintenance",
      "Only if the monitor breaks",
      "Only on school holidays"
    ],
    "options_hi": [
      "हाँ, इसे नियमित अपडेट और सही सेटिंग्स की आवश्यकता होती है",
      "नहीं, इसे कभी रखरखाव की आवश्यकता नहीं होती",
      "केवल तभी जब मॉनिटर टूट जाए",
      "केवल स्कूल की छुट्टियों के दौरान"
    ],
    "answer": "Yes",
    "correctAnswerIndex": 0,
    "explanation": "Firewall software vulnerabilities require regular vendor patching and continuous rule tuning.",
    "explanation_en": "Firewall software vulnerabilities require regular vendor patching and continuous rule tuning.",
    "explanation_hi": "फ़ायरवॉल को भी सुरक्षा खामियों से बचाने के लिए नियमित सॉफ़्टवेयर अपडेट और सही सेटिंग्स की आवश्यकता होती है।"
  },

  # Topic 8 (L2 T3): Proxy Firewall (Application-Level Gateway)
  {
    "id": "L2_T3_SCH_01",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "What is the role of a proxy firewall?",
    "question_en": "What is the role of a proxy firewall?",
    "question_hi": "प्रॉक्सी फ़ायरवॉल (Proxy Firewall) की क्या भूमिका होती है?",
    "options": [
      "It acts as an intermediary and can inspect application traffic",
      "It replaces the computer's screen",
      "It stores only photos",
      "It changes the weather"
    ],
    "options_en": [
      "It acts as an intermediary and can inspect application traffic",
      "It replaces the computer's screen",
      "It stores only photos",
      "It changes the weather"
    ],
    "options_hi": [
      "यह एक मध्यस्थ (Intermediary) के रूप में कार्य करता है और एप्लिकेशन ट्रैफ़िक की जांच करता है",
      "यह कंप्यूटर की स्क्रीन को बदल देता है",
      "यह केवल तस्वीरें संग्रहीत करता है",
      "यह मौसम बदलता है"
    ],
    "answer": "It acts as an intermediary and can inspect application traffic",
    "correctAnswerIndex": 0,
    "explanation": "Proxy firewalls mediate requests between clients and destinations, performing deep application inspection.",
    "explanation_en": "Proxy firewalls mediate requests between clients and destinations, performing deep application inspection.",
    "explanation_hi": "प्रॉक्सी फ़ायरवॉल आपके कंप्यूटर और इंटरनेट के बीच एक बिचौलिए की तरह काम करता है और डेटा की गहराई से जांच करता है।"
  },
  {
    "id": "L2_T3_SCH_02",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "A school uses a proxy to apply web access rules. What can it help do?",
    "question_en": "A school uses a proxy to apply web access rules. What can it help do?",
    "question_hi": "एक स्कूल वेब एक्सेस नियम लागू करने के लिए प्रॉक्सी का उपयोग करता है। यह क्या करने में मदद कर सकता है?",
    "options": [
      "Control access to selected websites or services",
      "Guarantee every website is safe",
      "Create unlimited internet speed",
      "Remove the need for user accounts"
    ],
    "options_en": [
      "Control access to selected websites or services",
      "Guarantee every website is safe",
      "Create unlimited internet speed",
      "Remove the need for user accounts"
    ],
    "options_hi": [
      "चयनित वेबसाइटों या हानिकारक सामग्री तक पहुँच को नियंत्रित/ब्लॉक करना",
      "गारंटी देना कि हर वेबसाइट सुरक्षित है",
      "असीमित इंटरनेट गति बनाना",
      "उपयोगकर्ता खातों की आवश्यकता को हटाना"
    ],
    "answer": "Control access to selected websites or services",
    "correctAnswerIndex": 0,
    "explanation": "Web proxies enforce organizational content filters, blocking inappropriate or malicious web categories.",
    "explanation_en": "Web proxies enforce organizational content filters, blocking inappropriate or malicious web categories.",
    "explanation_hi": "प्रॉक्सी स्कूल में छात्रों को हानिकारक या अनुपयुक्त वेबसाइटों से बचाकर केवल सुरक्षित वेबसाइट खोलने की अनुमति देता है।"
  },
  {
    "id": "L2_T3_SCH_03",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Why might a proxy firewall provide more application-level detail than a simple packet filter?",
    "question_en": "Why might a proxy firewall provide more application-level detail than a simple packet filter?",
    "question_hi": "प्रॉक्सी फ़ायरवॉल एक साधारण पैकेट फ़िल्टर की तुलना में अधिक एप्लिकेशन-स्तरीय विवरण क्यों प्रदान कर सकता है?",
    "options": [
      "It can examine supported application requests",
      "It only checks the screen size",
      "It cannot process network traffic",
      "It checks the user's handwriting"
    ],
    "options_en": [
      "It can examine supported application requests",
      "It only checks the screen size",
      "It cannot process network traffic",
      "It checks the user's handwriting"
    ],
    "options_hi": [
      "यह एप्लिकेशन प्रोटोकॉल (जैसे HTTP/FTP कमांड और अनुरोध) की पूरी जांच कर सकता है",
      "यह केवल स्क्रीन का आकार जाँचता है",
      "यह नेटवर्क ट्रैफ़िक को संसाधित नहीं कर सकता",
      "यह उपयोगकर्ता की लिखावट की जांच करता है"
    ],
    "answer": "It can examine supported application requests",
    "correctAnswerIndex": 0,
    "explanation": "Proxies terminate connections at Layer 7, letting them analyze HTTP methods, headers, and payloads.",
    "explanation_en": "Proxies terminate connections at Layer 7, letting them analyze HTTP methods, headers, and payloads.",
    "explanation_hi": "प्रॉक्सी एप्लिकेशन लेयर पर काम करता है, इसलिए यह वेब अनुरोधों और उनके अंदर मौजूद डेटा की पूरी जांच कर सकता है।"
  },
  {
    "id": "L2_T3_SCH_04",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "What is a possible limitation of a proxy firewall?",
    "question_en": "What is a possible limitation of a proxy firewall?",
    "question_hi": "प्रॉक्सी फ़ायरवॉल की एक संभावित सीमा (कमी) क्या हो सकती है?",
    "options": [
      "It may not inspect every protocol or threat equally well",
      "It always blocks all internet access",
      "It makes all passwords public",
      "It prevents the need for backups"
    ],
    "options_en": [
      "It may not inspect every protocol or threat equally well",
      "It always blocks all internet access",
      "It makes all passwords public",
      "It prevents the need for backups"
    ],
    "options_hi": [
      "यह हर प्रोटोकॉल या खतरे का समान रूप से अच्छा निरीक्षण नहीं कर सकता है (और गति थोड़ी धीमी हो सकती है)",
      "यह हमेशा सभी इंटरनेट एक्सेस को ब्लॉक करता है",
      "यह सभी पासवर्ड सार्वजनिक कर देता है",
      "यह बैकअप की आवश्यकता को रोकता है"
    ],
    "answer": "It may not inspect every protocol or threat equally well",
    "correctAnswerIndex": 0,
    "explanation": "Proxies require dedicated application support and may add latency or fail on unsupported protocols.",
    "explanation_en": "Proxies require dedicated application support and may add latency or fail on unsupported protocols.",
    "explanation_hi": "प्रॉक्सी हर प्रोटोकॉल के साथ काम नहीं कर सकता और गहरी जांच के कारण नेटवर्क गति पर थोड़ा असर पड़ सकता है।"
  },
  {
    "id": "L2_T3_SCH_05",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Which action is safest if a proxy blocks a website needed for class?",
    "question_en": "Which action is safest if a proxy blocks a website needed for class?",
    "question_hi": "यदि प्रॉक्सी कक्षा के लिए आवश्यक किसी वेबसाइट को ब्लॉक कर देता है तो सबसे सुरक्षित कदम क्या है?",
    "options": [
      "Ask IT support to review it",
      "Try to bypass school rules secretly",
      "Install an unknown proxy app",
      "Share the administrator password"
    ],
    "options_en": [
      "Ask IT support to review it",
      "Try to bypass school rules secretly",
      "Install an unknown proxy app",
      "Share the administrator password"
    ],
    "options_hi": [
      "IT सहायता या शिक्षक से इसकी समीक्षा और अनुमति देने का अनुरोध करें",
      "स्कूल के नियमों को चुपके से बायपास करने का प्रयास करें",
      "कोई अनजान प्रॉक्सी या वीपीएन ऐप इंस्टॉल करें",
      "व्यवस्थापक पासवर्ड साझा करें"
    ],
    "answer": "Ask IT support to review it",
    "correctAnswerIndex": 0,
    "explanation": "Never attempt to bypass security filters using sketchy bypass proxies; request IT review.",
    "explanation_en": "Never attempt to bypass security filters using sketchy bypass proxies; request IT review.",
    "explanation_hi": "असुरक्षित बायपास टूल इस्तेमाल करने के बजाय अपने IT शिक्षक से उस वेबसाइट को खोलने का अनुरोध करें।"
  },
  {
    "id": "L2_T3_SCH_06",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Does a proxy firewall guarantee that a downloaded file is harmless?",
    "question_en": "Does a proxy firewall guarantee that a downloaded file is harmless?",
    "question_hi": "क्या प्रॉक्सी फ़ायरवॉल यह गारंटी देता है कि डाउनलोड की गई फ़ाइल पूरी तरह से हानिरहित है?",
    "options": [
      "Yes",
      "No, other security checks may still be needed",
      "Only if it has a colourful icon",
      "Only on a phone"
    ],
    "options_en": [
      "Yes",
      "No, other security checks may still be needed",
      "Only if it has a colourful icon",
      "Only on a phone"
    ],
    "options_hi": [
      "हाँ, पूरी गारंटी देता है",
      "नहीं, एंटीवायरस जैसे अन्य सुरक्षा जांचों की अभी भी आवश्यकता हो सकती है",
      "केवल तभी जब उसका आइकन रंगीन हो",
      "केवल फ़ोन पर"
    ],
    "answer": "No, other security checks may still be needed",
    "correctAnswerIndex": 1,
    "explanation": "Proxies provide boundary filtering, but endpoint antivirus and malware scans remain vital.",
    "explanation_en": "Proxies provide boundary filtering, but endpoint antivirus and malware scans remain vital.",
    "explanation_hi": "प्रॉक्सी सुरक्षा का एक स्तर है, लेकिन डाउनलोड की गई फ़ाइलों को एंटीवायरस से जांचना फिर भी ज़रूरी है।"
  },
  {
    "id": "L2_T3_SCH_07",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Why should proxy access logs be handled carefully?",
    "question_en": "Why should proxy access logs be handled carefully?",
    "question_hi": "प्रॉक्सी एक्सेस लॉग्स (Proxy Logs) को सावधानी से क्यों संभाला जाना चाहिए?",
    "options": [
      "They may contain information about users' activity",
      "They contain no useful information ever",
      "They are always public",
      "They replace all passwords"
    ],
    "options_en": [
      "They may contain information about users' activity",
      "They contain no useful information ever",
      "They are always public",
      "They replace all passwords"
    ],
    "options_hi": [
      "वे उपयोगकर्ताओं की ब्राउज़िंग गतिविधि और निजी जानकारी रख सकते हैं",
      "उनमें कभी कोई उपयोगी जानकारी नहीं होती",
      "वे हमेशा सार्वजनिक होते हैं",
      "वे सभी पासवर्ड की जगह लेते हैं"
    ],
    "answer": "They may contain information about users' activity",
    "correctAnswerIndex": 0,
    "explanation": "Proxy logs record URLs visited, usernames, and timestamps, which represent sensitive personal data.",
    "explanation_en": "Proxy logs record URLs visited, usernames, and timestamps, which represent sensitive personal data.",
    "explanation_hi": "प्रॉक्सी लॉग्स में यह दर्ज होता है कि किसने कौन सी वेबसाइट कब देखी, जो कि निजी जानकारी है।"
  },
  {
    "id": "L2_T3_SCH_08",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Which describes an application-level gateway?",
    "question_en": "Which describes an application-level gateway?",
    "question_hi": "एप्लिकेशन-लेवल गेटवे (Application-Level Gateway) का क्या अर्थ है?",
    "options": [
      "A proxy that handles traffic for specific applications or protocols",
      "A type of computer chair",
      "A tool for drawing icons",
      "A battery charger"
    ],
    "options_en": [
      "A proxy that handles traffic for specific applications or protocols",
      "A type of computer chair",
      "A tool for drawing icons",
      "A battery charger"
    ],
    "options_hi": [
      "एक प्रॉक्सी जो विशिष्ट अनुप्रयोगों या प्रोटोकॉल (जैसे HTTP/FTP) के ट्रैफ़िक को संभालता है",
      "एक प्रकार की कंप्यूटर कुर्सी",
      "आइकन बनाने का टूल",
      "एक बैटरी चार्जर"
    ],
    "answer": "A proxy that handles traffic for specific applications or protocols",
    "correctAnswerIndex": 0,
    "explanation": "An Application-Level Gateway is a proxy tailored to decode and filter specific application layer traffic.",
    "explanation_en": "An Application-Level Gateway is a proxy tailored to decode and filter specific application layer traffic.",
    "explanation_hi": "यह एक ऐसी प्रॉक्सी प्रणाली है जो विशेष अनुप्रयोगों के ट्रैफ़िक की विस्तृत जांच करती है।"
  },
  {
    "id": "L2_T3_SCH_09",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "What should be true of proxy configuration?",
    "question_en": "What should be true of proxy configuration?",
    "question_hi": "प्रॉक्सी कॉन्फ़िगरेशन (Proxy Configuration) के बारे में क्या सही होना चाहिए?",
    "options": [
      "It should follow the organization's security and privacy rules",
      "It should be shared with strangers",
      "It should allow every connection by default",
      "It should never be reviewed"
    ],
    "options_en": [
      "It should follow the organization's security and privacy rules",
      "It should be shared with strangers",
      "It should allow every connection by default",
      "It should never be reviewed"
    ],
    "options_hi": [
      "इसे संगठन (स्कूल) के सुरक्षा और गोपनीयता नियमों का पालन करना चाहिए",
      "इसे अजनबियों के साथ साझा किया जाना चाहिए",
      "इसे डिफ़ॉल्ट रूप से हर कनेक्शन की अनुमति देनी चाहिए",
      "इसकी कभी समीक्षा नहीं की जानी चाहिए"
    ],
    "answer": "It should follow the organization's security and privacy rules",
    "correctAnswerIndex": 0,
    "explanation": "Proxy configurations must adhere to institutional Acceptable Use Policies and privacy guidelines.",
    "explanation_en": "Proxy configurations must adhere to institutional Acceptable Use Policies and privacy guidelines.",
    "explanation_hi": "प्रॉक्सी की सेटिंग्स स्कूल के सुरक्षा दिशा-निर्देशों और छात्र सुरक्षा नीतियों के अनुरूप होनी चाहिए।"
  },
  {
    "id": "L2_T3_SCH_10",
    "level": 2,
    "topic": "Proxy Firewall (Application-Level Gateway)",
    "topicId": "proxy_firewall",
    "mode": "school",
    "question": "Why might a proxy be used together with other security tools?",
    "question_en": "Why might a proxy be used together with other security tools?",
    "question_hi": "प्रॉक्सी का उपयोग अन्य सुरक्षा उपकरणों के साथ मिलकर क्यों किया जाता है?",
    "options": [
      "Different tools protect against different risks",
      "A proxy makes other tools illegal",
      "It removes all cyber threats",
      "It makes updates unnecessary"
    ],
    "options_en": [
      "Different tools protect against different risks",
      "A proxy makes other tools illegal",
      "It removes all cyber threats",
      "It makes updates unnecessary"
    ],
    "options_hi": [
      "अलग-अलग उपकरण अलग-अलग जोखिमों से रक्षा करते हैं (रक्षा में गहराई / Defense in Depth)",
      "प्रॉक्सी अन्य उपकरणों को अवैध बनाता है",
      "यह सभी साइबर खतरों को समाप्त करता है",
      "यह अपडेट को अनावश्यक बनाता है"
    ],
    "answer": "Different tools protect against different risks",
    "correctAnswerIndex": 0,
    "explanation": "Defense in depth combines proxies, firewalls, and endpoint antivirus to mitigate diverse attack vectors.",
    "explanation_en": "Defense in depth combines proxies, firewalls, and endpoint antivirus to mitigate diverse attack vectors.",
    "explanation_hi": "मजबूत सुरक्षा के लिए बहु-स्तरीय सुरक्षा (फ़ायरवॉल, प्रॉक्सी और एंटीवायरस) एक साथ काम करते हैं।"
  },

  # Topic 9 (L2 T4): Cloud Firewall
  {
    "id": "L2_T4_SCH_01",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "What does a cloud firewall help protect?",
    "question_en": "What does a cloud firewall help protect?",
    "question_hi": "क्लाउड फ़ायरवॉल (Cloud Firewall) किसकी सुरक्षा में मदद करता है?",
    "options": [
      "Cloud networks, workloads, or services by controlling traffic",
      "Only printed paper",
      "A classroom whiteboard",
      "A phone's ringtone"
    ],
    "options_en": [
      "Cloud networks, workloads, or services by controlling traffic",
      "Only printed paper",
      "A classroom whiteboard",
      "A phone's ringtone"
    ],
    "options_hi": [
      "ट्रैफ़िक को नियंत्रित करके क्लाउड नेटवर्क, सर्वर और ऑनलाइन सेवाओं की",
      "केवल मुद्रित कागज़ की",
      "कक्षा के व्हाइटबोर्ड की",
      "फ़ोन की रिंगटोन की"
    ],
    "answer": "Cloud networks, workloads, or services by controlling traffic",
    "correctAnswerIndex": 0,
    "explanation": "Cloud firewalls filter virtual traffic around cloud-hosted servers, containers, and web applications.",
    "explanation_en": "Cloud firewalls filter virtual traffic around cloud-hosted servers, containers, and web applications.",
    "explanation_hi": "क्लाउड फ़ायरवॉल इंटरनेट पर चलने वाले क्लाउड सर्वर और ऐप्स की अनधिकृत ट्रैफ़िक से रक्षा करता है।"
  },
  {
    "id": "L2_T4_SCH_02",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "A cloud server should accept web traffic but not remote administration from everyone. What should be configured?",
    "question_en": "A cloud server should accept web traffic but not remote administration from everyone. What should be configured?",
    "question_hi": "एक क्लाउड सर्वर को वेब ट्रैफ़िक स्वीकार करना चाहिए लेकिन हर किसी से रिमोट एडमिनिस्ट्रेशन नहीं। क्या कॉन्फ़िगर किया जाना चाहिए?",
    "options": [
      "Rules that allow required web traffic and restrict administration access",
      "A rule allowing all ports to everyone",
      "No access controls",
      "A public password list"
    ],
    "options_en": [
      "Rules that allow required web traffic and restrict administration access",
      "A rule allowing all ports to everyone",
      "No access controls",
      "A public password list"
    ],
    "options_hi": [
      "नियम जो केवल आवश्यक वेब ट्रैफ़िक की अनुमति दें और एडमिन पहुँच को प्रतिबंधित करें",
      "एक नियम जो सभी को सभी पोर्ट्स की अनुमति दे",
      "कोई एक्सेस नियंत्रण नहीं",
      "एक सार्वजनिक पासवर्ड सूची"
    ],
    "answer": "Rules that allow required web traffic and restrict administration access",
    "correctAnswerIndex": 0,
    "explanation": "Open public ports 80/443 for web users, but strictly restrict SSH/RDP ports to authorized IP ranges.",
    "explanation_en": "Open public ports 80/443 for web users, but strictly restrict SSH/RDP ports to authorized IP ranges.",
    "explanation_hi": "वेबसाइट के लिए पोर्ट खुला रखें लेकिन सर्वर प्रबंधन (SSH/RDP) केवल अधिकृत एडमिन के लिए ही सीमित करें।"
  },
  {
    "id": "L2_T4_SCH_03",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Why should cloud firewall rules follow least privilege?",
    "question_en": "Why should cloud firewall rules follow least privilege?",
    "question_hi": "क्लाउड फ़ायरवॉल नियमों को न्यूनतम विशेषाधिकार (Least Privilege) का पालन क्यों करना चाहिए?",
    "options": [
      "Only necessary connections should be allowed",
      "All services should be public",
      "No one should use updates",
      "It makes passwords shorter"
    ],
    "options_en": [
      "Only necessary connections should be allowed",
      "All services should be public",
      "No one should use updates",
      "It makes passwords shorter"
    ],
    "options_hi": [
      "केवल अत्यंत आवश्यक कनेक्शनों को ही अनुमति दी जानी चाहिए",
      "सभी सेवाओं को सार्वजनिक होना चाहिए",
      "किसी को अपडेट का उपयोग नहीं करना चाहिए",
      "यह पासवर्ड को छोटा बनाता है"
    ],
    "answer": "Only necessary connections should be allowed",
    "correctAnswerIndex": 0,
    "explanation": "Principle of least privilege ensures cloud environments expose minimal surface area to potential attackers.",
    "explanation_en": "Principle of least privilege ensures cloud environments expose minimal surface area to potential attackers.",
    "explanation_hi": "कम से कम विशेषाधिकार का अर्थ है कि केवल वही पोर्ट या कनेक्शन खोले जाएं जिनकी असली ज़रूरत हो।"
  },
  {
    "id": "L2_T4_SCH_04",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Who should normally manage an organization's cloud firewall?",
    "question_en": "Who should normally manage an organization's cloud firewall?",
    "question_hi": "किसी संगठन के क्लाउड फ़ायरवॉल का प्रबंधन सामान्यतः किसे करना चाहिए?",
    "options": [
      "An authorized cloud or IT administrator",
      "Any anonymous visitor",
      "A random game player",
      "Everyone on public Wi-Fi"
    ],
    "options_en": [
      "An authorized cloud or IT administrator",
      "Any anonymous visitor",
      "A random game player",
      "Everyone on public Wi-Fi"
    ],
    "options_hi": [
      "एक अधिकृत क्लाउड या IT व्यवस्थापक (Administrator)",
      "कोई भी अज्ञात आगंतुक",
      "कोई भी रैंडम गेम खिलाड़ी",
      "सार्वजनिक वाई-फ़ाई पर मौजूद हर कोई"
    ],
    "answer": "An authorized cloud or IT administrator",
    "correctAnswerIndex": 0,
    "explanation": "Only authorized cloud architects and administrators possess the credentials to modify security groups.",
    "explanation_en": "Only authorized cloud architects and administrators possess the credentials to modify security groups.",
    "explanation_hi": "क्लाउड फ़ायरवॉल की सेटिंग्स केवल अधिकृत क्लाउड या नेटवर्क इंजीनियर को ही बदलनी चाहिए।"
  },
  {
    "id": "L2_T4_SCH_05",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "What is one risk of leaving a cloud service unnecessarily exposed to the internet?",
    "question_en": "What is one risk of leaving a cloud service unnecessarily exposed to the internet?",
    "question_hi": "किसी क्लाउड सेवा को इंटरनेट पर अनावश्यक रूप से खुला छोड़ने का एक जोखिम क्या है?",
    "options": [
      "Attackers may have more opportunities to reach it",
      "It guarantees better security",
      "It prevents every login",
      "It creates offline backups"
    ],
    "options_en": [
      "Attackers may have more opportunities to reach it",
      "It guarantees better security",
      "It prevents every login",
      "It creates offline backups"
    ],
    "options_hi": [
      "हमलावरों को उस तक पहुँचने और शोषण करने के अधिक अवसर मिल सकते हैं",
      "यह बेहतर सुरक्षा की गारंटी देता है",
      "यह हर लॉगिन को रोकता है",
      "यह ऑफ़लाइन बैकअप बनाता है"
    ],
    "answer": "Attackers may have more opportunities to reach it",
    "correctAnswerIndex": 0,
    "explanation": "Unnecessary internet exposure allows automated bots to scan and exploit unpatched vulnerabilities.",
    "explanation_en": "Unnecessary internet exposure allows automated bots to scan and exploit unpatched vulnerabilities.",
    "explanation_hi": "यदि कोई डेटाबेस या सर्वर बिना सुरक्षा के इंटरनेट पर खुला छोड़ दिया जाए तो हैकर्स उस पर आसानी से हमला कर सकते हैं।"
  },
  {
    "id": "L2_T4_SCH_06",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Why review cloud firewall rules after a project ends?",
    "question_en": "Why review cloud firewall rules after a project ends?",
    "question_hi": "कोई प्रोजेक्ट समाप्त होने के बाद क्लाउड फ़ायरवॉल नियमों की समीक्षा क्यों करनी चाहिए?",
    "options": [
      "Old access may no longer be needed",
      "The rules become a game",
      "Passwords stop existing",
      "The internet disappears"
    ],
    "options_en": [
      "Old access may no longer be needed",
      "The rules become a game",
      "Passwords stop existing",
      "The internet disappears"
    ],
    "options_hi": [
      "पुरानी अनुमतियों की अब आवश्यकता नहीं हो सकती है और उन्हें बंद करना ज़रूरी है",
      "नियम एक खेल बन जाते हैं",
      "पासवर्ड समाप्त हो जाते हैं",
      "इंटरनेट गायब हो जाता है"
    ],
    "answer": "Old access may no longer be needed",
    "correctAnswerIndex": 0,
    "explanation": "Temporary development rules left open create security loopholes after project completion.",
    "explanation_en": "Temporary development rules left open create security loopholes after project completion.",
    "explanation_hi": "प्रोजेक्ट खत्म होने पर पुराने अस्थायी नियमों को बंद करना चाहिए ताकि कोई पुराना खुला दरवाजा सुरक्षा में सेंध न लगाए।"
  },
  {
    "id": "L2_T4_SCH_07",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Can cloud firewalls be used with other cloud security controls?",
    "question_en": "Can cloud firewalls be used with other cloud security controls?",
    "question_hi": "क्या क्लाउड फ़ायरवॉल का उपयोग अन्य क्लाउड सुरक्षा नियंत्रणों के साथ किया जा सकता है?",
    "options": [
      "Yes",
      "No, only one security control is allowed",
      "Only on paper",
      "Only when no data exists"
    ],
    "options_en": [
      "Yes",
      "No, only one security control is allowed",
      "Only on paper",
      "Only when no data exists"
    ],
    "options_hi": [
      "हाँ, बहु-स्तरीय सुरक्षा के लिए अन्य टूल्स के साथ मिलाकर उपयोग किया जाता है",
      "नहीं, केवल एक सुरक्षा नियंत्रण की अनुमति है",
      "केवल कागज़ पर",
      "केवल जब कोई डेटा मौजूद न हो"
    ],
    "answer": "Yes",
    "correctAnswerIndex": 0,
    "explanation": "Cloud security works best when combining network firewalls, IAM policies, and encryption.",
    "explanation_en": "Cloud security works best when combining network firewalls, IAM policies, and encryption.",
    "explanation_hi": "क्लाउड फ़ायरवॉल को IAM (पहचान प्रबंधन), एन्क्रिप्शन और WAF के साथ मिलाकर उपयोग किया जाता है।"
  },
  {
    "id": "L2_T4_SCH_08",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "What should you do before changing a production firewall rule?",
    "question_en": "What should you do before changing a production firewall rule?",
    "question_hi": "प्रोडक्शन फ़ायरवॉल नियम बदलने से पहले क्या करना चाहिए?",
    "options": [
      "Follow approval and testing procedures",
      "Change every rule at random",
      "Share admin credentials publicly",
      "Disable monitoring"
    ],
    "options_en": [
      "Follow approval and testing procedures",
      "Change every rule at random",
      "Share admin credentials publicly",
      "Disable monitoring"
    ],
    "options_hi": [
      "स्वीकृति और परीक्षण प्रक्रियाओं (Approval & Testing) का पालन करें",
      "हर नियम को यादृच्छिक रूप से बदलें",
      "व्यवस्थापक क्रेडेंशियल सार्वजनिक रूप से साझा करें",
      "निगरानी अक्षम करें"
    ],
    "answer": "Follow approval and testing procedures",
    "correctAnswerIndex": 0,
    "explanation": "Change management protocols prevent accidental service outages and unintended security gaps.",
    "explanation_en": "Change management protocols prevent accidental service outages and unintended security gaps.",
    "explanation_hi": "नियम बदलने से पहले उसका परीक्षण करना चाहिए ताकि वास्तविक सेवाएं बाधित न हों।"
  },
  {
    "id": "L2_T4_SCH_09",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Which is a safer approach to remote administration?",
    "question_en": "Which is a safer approach to remote administration?",
    "question_hi": "रिमोट एडमिनिस्ट्रेशन (दूरस्थ प्रबंधन) के लिए कौन सा तरीका अधिक सुरक्षित है?",
    "options": [
      "Restrict it to approved users and trusted access paths",
      "Allow all internet users",
      "Use no authentication",
      "Publish the admin password"
    ],
    "options_en": [
      "Restrict it to approved users and trusted access paths",
      "Allow all internet users",
      "Use no authentication",
      "Publish the admin password"
    ],
    "options_hi": [
      "इसे केवल स्वीकृत उपयोगकर्ताओं और विश्वसनीय पहुँच मार्गों (जैसे VPN/Bastion) तक सीमित करना",
      "सभी इंटरनेट उपयोगकर्ताओं को अनुमति देना",
      "किसी प्रमाणीकरण का उपयोग न करना",
      "व्यवस्थापक पासवर्ड प्रकाशित करना"
    ],
    "answer": "Restrict it to approved users and trusted access paths",
    "correctAnswerIndex": 0,
    "explanation": "Admin consoles must never be exposed publicly; restrict them via jump boxes, VPNs, and MFA.",
    "explanation_en": "Admin consoles must never be exposed publicly; restrict them via jump boxes, VPNs, and MFA.",
    "explanation_hi": "सर्वर का एडमिन एक्सेस कभी इंटरनेट पर खुला नहीं होना चाहिए; इसे केवल सुरक्षित VPN के ज़रिए ही खोला जाना चाहिए।"
  },
  {
    "id": "L2_T4_SCH_10",
    "level": 2,
    "topic": "Cloud Firewall",
    "topicId": "cloud_firewall",
    "mode": "school",
    "question": "Does a cloud firewall alone make a cloud application completely secure?",
    "question_en": "Does a cloud firewall alone make a cloud application completely secure?",
    "question_hi": "क्या केवल क्लाउड फ़ायरवॉल ही किसी क्लाउड एप्लिकेशन को पूरी तरह से सुरक्षित बना देता है?",
    "options": [
      "Yes",
      "No, application security, identity controls, and updates also matter",
      "Only at night",
      "Only if it has a logo"
    ],
    "options_en": [
      "Yes",
      "No, application security, identity controls, and updates also matter",
      "Only at night",
      "Only if it has a logo"
    ],
    "options_hi": [
      "हाँ, अकेला काफी है",
      "नहीं; एप्लिकेशन सुरक्षा, पहचान नियंत्रण और अपडेट भी समान रूप से महत्वपूर्ण हैं",
      "केवल रात में",
      "केवल अगर इसका लोगो हो"
    ],
    "answer": "No, application security, identity controls, and updates also matter",
    "correctAnswerIndex": 1,
    "explanation": "Security requires defense in depth across code, identity, configuration, and data layers.",
    "explanation_en": "Security requires defense in depth across code, identity, configuration, and data layers.",
    "explanation_hi": "फ़ायरवॉल के साथ-साथ मजबूत पासवर्ड, सुरक्षित कोडिंग और सॉफ़्टवेयर अपडेट भी ज़रूरी होते हैं।"
  },

  # Topic 10 (L2 T5): Software Firewall
  {
    "id": "L2_T5_SCH_01",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Where does a software firewall commonly operate?",
    "question_en": "Where does a software firewall commonly operate?",
    "question_hi": "सॉफ़्टवेयर फ़ायरवॉल आमतौर पर कहाँ काम करता है?",
    "options": [
      "On a computer or server",
      "Only inside a paper notebook",
      "Only in a power cable",
      "Inside a school bell"
    ],
    "options_en": [
      "On a computer or server",
      "Only inside a paper notebook",
      "Only in a power cable",
      "Inside a school bell"
    ],
    "options_hi": [
      "सीधे किसी कंप्यूटर, लैपटॉप या सर्वर के ऑपरेटिंग सिस्टम पर",
      "केवल एक कागज़ की नोटबुक के अंदर",
      "केवल पावर केबल में",
      "स्कूल की घंटी के अंदर"
    ],
    "answer": "On a computer or server",
    "correctAnswerIndex": 0,
    "explanation": "Host-based software firewalls run locally inside operating systems (like Windows Defender Firewall).",
    "explanation_en": "Host-based software firewalls run locally inside operating systems (like Windows Defender Firewall).",
    "explanation_hi": "सॉफ़्टवेयर फ़ायरवॉल आपके कंप्यूटर या लैपटॉप के ऑपरेटिंग सिस्टम में इनबिल्ट प्रोग्राम के रूप में चलता है।"
  },
  {
    "id": "L2_T5_SCH_02",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "A laptop firewall asks whether an unfamiliar app may accept connections. What is sensible?",
    "question_en": "A laptop firewall asks whether an unfamiliar app may accept connections. What is sensible?",
    "question_hi": "लैपटॉप का फ़ायरवॉल पूछता है कि क्या कोई अपरिचित ऐप नेटवर्क कनेक्शन स्वीकार कर सकता है। क्या समझदारी भरा कदम है?",
    "options": [
      "Check what the app is and allow only if needed and trusted",
      "Always allow every app",
      "Share the alert online with passwords",
      "Disable updates"
    ],
    "options_en": [
      "Check what the app is and allow only if needed and trusted",
      "Always allow every app",
      "Share the alert online with passwords",
      "Disable updates"
    ],
    "options_hi": [
      "जांचें कि ऐप क्या है और केवल तभी अनुमति दें जब वह आवश्यक और विश्वसनीय हो",
      "हमेशा हर ऐप को अनुमति दें",
      "पासवर्ड के साथ चेतावनी को ऑनलाइन साझा करें",
      "अपडेट अक्षम करें"
    ],
    "answer": "Check what the app is and allow only if needed and trusted",
    "correctAnswerIndex": 0,
    "explanation": "Verify the program's signature and necessity before granting inbound network privileges.",
    "explanation_en": "Verify the program's signature and necessity before granting inbound network privileges.",
    "explanation_hi": "अपरिचित ऐप को नेटवर्क से कनेक्ट करने की अनुमति देने से पहले यह जानना ज़रूरी है कि वह सुरक्षित है या नहीं।"
  },
  {
    "id": "L2_T5_SCH_03",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "What is a key difference between a host-based firewall and a network firewall?",
    "question_en": "What is a key difference between a host-based firewall and a network firewall?",
    "question_hi": "होस्ट-आधारित (सॉफ़्टवेयर) फ़ायरवॉल और नेटवर्क फ़ायरवॉल के बीच मुख्य अंतर क्या है?",
    "options": [
      "A host-based firewall protects an individual device",
      "A host-based firewall only protects buildings",
      "A network firewall is a password manager",
      "There is never any difference"
    ],
    "options_en": [
      "A host-based firewall protects an individual device",
      "A host-based firewall only protects buildings",
      "A network firewall is a password manager",
      "There is never any difference"
    ],
    "options_hi": [
      "होस्ट-आधारित फ़ायरवॉल किसी व्यक्तिगत डिवाइस की सुरक्षा करता है जबकि नेटवर्क फ़ायरवॉल पूरे नेटवर्क की",
      "होस्ट-आधारित फ़ायरवॉल केवल इमारतों की सुरक्षा करता है",
      "नेटवर्क फ़ायरवॉल एक पासवर्ड मैनेजर है",
      "इनमें कभी कोई अंतर नहीं होता"
    ],
    "answer": "A host-based firewall protects an individual device",
    "correctAnswerIndex": 0,
    "explanation": "Host firewalls protect specific endpoints, whereas network firewalls protect entire subnet perimeters.",
    "explanation_en": "Host firewalls protect specific endpoints, whereas network firewalls protect entire subnet perimeters.",
    "explanation_hi": "होस्ट फ़ायरवॉल केवल उस कंप्यूटर की रक्षा करता है जिस पर वह इंस्टॉल है, जबकि नेटवर्क फ़ायरवॉल कई कंप्यूटरों को बचाता है।"
  },
  {
    "id": "L2_T5_SCH_04",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Why should a software firewall remain enabled?",
    "question_en": "Why should a software firewall remain enabled?",
    "question_hi": "सॉफ़्टवेयर फ़ायरवॉल को हमेशा सक्षम (Enabled/On) क्यों रखना चाहिए?",
    "options": [
      "It can help control unwanted connections to the device",
      "It guarantees no scams",
      "It makes every download safe",
      "It removes all need for passwords"
    ],
    "options_en": [
      "It can help control unwanted connections to the device",
      "It guarantees no scams",
      "It makes every download safe",
      "It removes all need for passwords"
    ],
    "options_hi": [
      "यह डिवाइस से होने वाले अवांछित और अनधिकृत कनेक्शनों को नियंत्रित करने में मदद करता है",
      "यह किसी घोटाले की गारंटी नहीं देता",
      "यह हर डाउनलोड को सुरक्षित बनाता है",
      "यह पासवर्ड की सभी ज़रूरतों को समाप्त कर देता है"
    ],
    "answer": "It can help control unwanted connections to the device",
    "correctAnswerIndex": 0,
    "explanation": "Enabled software firewalls protect the device from local subnet intrusions and rogue network traffic.",
    "explanation_en": "Enabled software firewalls protect the device from local subnet intrusions and rogue network traffic.",
    "explanation_hi": "फ़ायरवॉल ऑन रहने से कोई भी अनधिकृत प्रोग्राम या बाहरी कंप्यूटर आपके सिस्टम से सीधा संपर्क नहीं बना सकता।"
  },
  {
    "id": "L2_T5_SCH_05",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Who should approve firewall changes on a managed school laptop?",
    "question_en": "Who should approve firewall changes on a managed school laptop?",
    "question_hi": "स्कूल के प्रबंधित लैपटॉप पर फ़ायरवॉल परिवर्तनों को किसकी स्वीकृति मिलनी चाहिए?",
    "options": [
      "The authorized IT administrator or policy owner",
      "Any website",
      "An unknown caller",
      "A person sending a pop-up"
    ],
    "options_en": [
      "The authorized IT administrator or policy owner",
      "Any website",
      "An unknown caller",
      "A person sending a pop-up"
    ],
    "options_hi": [
      "अधिकृत IT व्यवस्थापक या स्कूल सुरक्षा नीति प्रमुख",
      "कोई भी वेबसाइट",
      "एक अज्ञात कॉलर",
      "पॉप-अप भेजने वाला व्यक्ति"
    ],
    "answer": "The authorized IT administrator or policy owner",
    "correctAnswerIndex": 0,
    "explanation": "Managed devices enforce organizational policies overseen exclusively by appointed IT staff.",
    "explanation_en": "Managed devices enforce organizational policies overseen exclusively by appointed IT staff.",
    "explanation_hi": "स्कूल के लैपटॉप पर सुरक्षा सेटिंग्स को बदलने का अधिकार केवल स्कूल के IT विभाग के पास होता है।"
  },
  {
    "id": "L2_T5_SCH_06",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "What should you do if a program suddenly requests unusual network access?",
    "question_en": "What should you do if a program suddenly requests unusual network access?",
    "question_hi": "यदि कोई प्रोग्राम अचानक असामान्य नेटवर्क एक्सेस का अनुरोध करता है तो आपको क्या करना चाहिए?",
    "options": [
      "Check with trusted IT support before allowing it",
      "Approve it automatically",
      "Send your password to the program",
      "Turn off the screen"
    ],
    "options_en": [
      "Check with trusted IT support before allowing it",
      "Approve it automatically",
      "Send your password to the program",
      "Turn off the screen"
    ],
    "options_hi": [
      "अनुमति देने से पहले विश्वसनीय IT सहायता या शिक्षक से जांच करें",
      "इसे स्वचालित रूप से स्वीकृत करें",
      "प्रोग्राम को अपना पासवर्ड भेजें",
      "स्क्रीन बंद कर दें"
    ],
    "answer": "Check with trusted IT support before allowing it",
    "correctAnswerIndex": 0,
    "explanation": "Sudden outbound requests may signify trojans establishing command-and-control communication.",
    "explanation_en": "Sudden outbound requests may signify trojans establishing command-and-control communication.",
    "explanation_hi": "यदि कोई अनजान ऐप इंटरनेट से जुड़ना चाहे तो उसे ब्लॉक करें और IT शिक्षक से पुष्टि करें।"
  },
  {
    "id": "L2_T5_SCH_07",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Can a software firewall control some outgoing connections as well as incoming ones?",
    "question_en": "Can a software firewall control some outgoing connections as well as incoming ones?",
    "question_hi": "क्या सॉफ़्टवेयर फ़ायरवॉल आने वाले (Incoming) कनेक्शनों के साथ-साथ जाने वाले (Outgoing) कनेक्शनों को भी नियंत्रित कर सकता है?",
    "options": [
      "Yes",
      "No, never",
      "Only when the laptop is closed",
      "Only on a printer"
    ],
    "options_en": [
      "Yes",
      "No, never",
      "Only when the laptop is closed",
      "Only on a printer"
    ],
    "options_hi": [
      "हाँ, यह दोनों प्रकार के कनेक्शनों को नियंत्रित कर सकता है",
      "नहीं, कभी नहीं",
      "केवल तभी जब लैपटॉप बंद हो",
      "केवल प्रिंटर पर"
    ],
    "answer": "Yes",
    "correctAnswerIndex": 0,
    "explanation": "Egress filtering in software firewalls stops unauthorized applications from exfiltrating data.",
    "explanation_en": "Egress filtering in software firewalls stops unauthorized applications from exfiltrating data.",
    "explanation_hi": "सॉफ़्टवेयर फ़ायरवॉल यह भी रोक सकता है कि कंप्यूटर के अंदर से कोई संदिग्ध ऐप बाहर डेटा न भेज सके।"
  },
  {
    "id": "L2_T5_SCH_08",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Why do firewall updates matter?",
    "question_en": "Why do firewall updates matter?",
    "question_hi": "फ़ायरवॉल अपडेट क्यों महत्वपूर्ण हैं?",
    "options": [
      "They can fix bugs and improve protection",
      "They make all accounts public",
      "They eliminate the need for backups",
      "They stop every phishing message"
    ],
    "options_en": [
      "They can fix bugs and improve protection",
      "They make all accounts public",
      "They eliminate the need for backups",
      "They stop every phishing message"
    ],
    "options_hi": [
      "वे सॉफ़्टवेयर की खामियों को ठीक कर सकते हैं और सुरक्षा को बेहतर बना सकते हैं",
      "वे सभी खातों को सार्वजनिक कर देते हैं",
      "वे बैकअप की आवश्यकता को समाप्त कर देते हैं",
      "वे हर फ़िशिंग संदेश को रोकते हैं"
    ],
    "answer": "They can fix bugs and improve protection",
    "correctAnswerIndex": 0,
    "explanation": "Software patches eliminate logic bugs and improve compatibility with modern networking protocols.",
    "explanation_en": "Software patches eliminate logic bugs and improve compatibility with modern networking protocols.",
    "explanation_hi": "नियमित अपडेट से फ़ायरवॉल के बग्स ठीक होते हैं और वह नए सुरक्षा खतरों को प्रभावी ढंग से रोक पाता है।"
  },
  {
    "id": "L2_T5_SCH_09",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "Which is an unsafe firewall habit?",
    "question_en": "Which is an unsafe firewall habit?",
    "question_hi": "इनमें से कौन सी एक असुरक्षित फ़ायरवॉल आदत है?",
    "options": [
      "Reviewing a rule carefully",
      "Allowing an unknown program without checking",
      "Keeping the firewall enabled",
      "Asking IT about an alert"
    ],
    "options_en": [
      "Reviewing a rule carefully",
      "Allowing an unknown program without checking",
      "Keeping the firewall enabled",
      "Asking IT about an alert"
    ],
    "options_hi": [
      "नियम की सावधानीपूर्वक समीक्षा करना",
      "बिना जांचे किसी अज्ञात प्रोग्राम को नेटवर्क पहुँच की अनुमति देना",
      "फ़ायरवॉल को हमेशा सक्षम रखना",
      "चेतावनी के बारे में IT से पूछना"
    ],
    "answer": "Allowing an unknown program without checking",
    "correctAnswerIndex": 1,
    "explanation": "Blindly clicking 'Allow' on unknown programs bypasses firewall protections for malicious binaries.",
    "explanation_en": "Blindly clicking 'Allow' on unknown programs bypasses firewall protections for malicious binaries.",
    "explanation_hi": "बिना सोचे-समझे किसी भी अनजान ऐप को फ़ायरवॉल में अनुमति देना मैलवेयर को खुला रास्ता दे सकता है।"
  },
  {
    "id": "L2_T5_SCH_10",
    "level": 2,
    "topic": "Software Firewall",
    "topicId": "software_firewall",
    "mode": "school",
    "question": "What is a firewall's main purpose?",
    "question_en": "What is a firewall's main purpose?",
    "question_hi": "फ़ायरवॉल का मुख्य उद्देश्य क्या है?",
    "options": [
      "Control network connections according to security rules",
      "Clean the physical keyboard",
      "Make a computer heavier",
      "Replace the operating system"
    ],
    "options_en": [
      "Control network connections according to security rules",
      "Clean the physical keyboard",
      "Make a computer heavier",
      "Replace the operating system"
    ],
    "options_hi": [
      "सुरक्षा नियमों के अनुसार नेटवर्क कनेक्शनों की निगरानी और नियंत्रण करना",
      "भौतिक कीबोर्ड को साफ़ करना",
      "कंप्यूटर को भारी बनाना",
      "ऑपरेटिंग सिस्टम को बदलना"
    ],
    "answer": "Control network connections according to security rules",
    "correctAnswerIndex": 0,
    "explanation": "Firewalls regulate communication into and out of systems according to designated security policies.",
    "explanation_en": "Firewalls regulate communication into and out of systems according to designated security policies.",
    "explanation_hi": "फ़ायरवॉल का मूल उद्देश्य सुरक्षा नियमों के अनुसार आने-जाने वाले सभी नेटवर्क ट्रैफ़िक को नियंत्रित करना है।"
  }
]

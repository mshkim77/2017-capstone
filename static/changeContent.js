

let ANNOYANCE_EN        = "Annoyance";      let ANNOYANCE_KO        = "성가심, 귀찮음, 괴로움";
let ANGER_EN            = "Anger";          let ANGER_KO            = "화, 분노";
let RAGE_EN             = "Rage";           let RAGE_KO             = "분노, 격노, 격분";

let INTEREST_EN         = "Interest";       let INTEREST_KO         = "흥미, 호기심, 관심";
let ANTICIPATION_EN     = "Anticipation";   let ANTICIPATION_KO     = "예측, 기대";
let VIGILANCE_EN        = "Vigilance";      let VIGILANCE_KO        = "경계, 조심";

let SERENITY_EN         = "Serenity";       let SERENITY_KO         = "안정, 평온, 차분함";
let JOY_EN              = "Joy";            let JOY_KO              = "기쁨, 환희, 만족";
let ECSTASY_EN          = "Ecstasy";        let ECSTASY_KO          = "황홀, 환희, 기쁨";

let ACCEPTANCE_EN       = "Acceptance";     let ACCEPTANCE_KO       = "수용, 묵인, 신봉";
let TRUST_EN            = "Trust";          let TRUST_KO            = "신뢰, 신임";
let ADMIRATION_EN       = "Admiration";     let ADMIRATION_KO       = "감탄, 존경, 탄복";

let APPREHENSION_EN     = "Apprehension";   let APPREHENSION_KO     = "불안, 걱정, 두려움";
let FEAR_EN             = "Fear";           let FEAR_KO             = "공포, 두려움, 무서움";
let TERROR_EN           = "Terror";         let TERROR_KO           = "공포, 끔찍함, 소름끼침";

let DISTRACTION_EN      = "Distraction";    let DISTRACTION_KO      = "주의 산만, 방심";
let SURPRISE_EN         = "Surprise";       let SURPRISE_KO         = "놀람, 경악";
let AMAZEMENT_EN        = "Amazement";      let AMAZEMENT_KO        = "놀림, 실색";

let PENSIVENESS_EN      = "Pensiveness";    let PENSIVENESS_KO      = "고뇌, 수심";
let SADNESS_EN          = "Sadness";        let SADNESS_KO          = "슬픔, 비애, 불행";
let GRIEF_EN            = "Grief";          let GRIEF_KO            = "고뇌, 한탄, 비통";

let BOREDOM_EN          = "Boredom";        let BOREDOM_KO          = "권태, 지루함, 따분함";
let DISGUST_EN          = "Disgust";        let DISGUST_KO          = "혐오, 역겨움, 넌더리";
let LOATHING_EN         = "Loathing";       let LOATHING_KO         = "혐오, 증오";

let AGGRESSIVENESS_EN   = "Aggressiveness"; let AGGRESSIVENESS_KO   = "공격성, 적극성";
let OPTIMISTIC_EN       = "Optimistic";     let OPTIMISTIC_KO       = "낙관, 긍정, 희망";
let LOVE_EN             = "Love";           let LOVE_KO             = "사랑, 기쁨";
let SUBMISSION_EN       = "Submission";     let SUBMISSION_KO       = "복종, 항복, 제안";
let AWE_EN              = "Awe";            let AWE_KO              = "경외감, 두려움";
let DISAPPROVAL_EN      = "Disapproval";    let DISAPPROVAL_KO      = "반감, 불만, 비난";
let REMORSE_EN          = "Remorse";        let REMORSE_KO          = "후회, 가책, 자책";
let CONTEMPT_EN         = "Contempt";       let CONTEMPT_KO         = "경멸, 멸시, 무시";



    function setDetailEmotion() {

        var box = document.getElementsByClassName("emotionBox");

        var deepHigh = 70;
        var deepLow = 40; 

        var space = box[0].getElementsByTagName("span");

        for (var i = 0; i < space.length; i = i + 3) {
            
            var emotion = space[i].innerHTML;
            var per = space[i+1].innerHTML.split("%")[0];
            var perNum = 0;

            var info = "";
            
            switch(emotion) {
                case ANNOYANCE_EN:
                    if(per >= deepHigh) {
                        info = RAGE_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = ANGER_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = ANNOYANCE_EN;
                        perNum = per * 3;
                    }
                    break;

                case INTEREST_EN :
                    if(per >= deepHigh) {
                        info = VIGILANCE_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = ANTICIPATION_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = INTEREST_EN;
                        perNum = per * 3;
                    }
                    break;

                case SERENITY_EN :
                    if(per >= deepHigh) {
                        info = ECSTASY_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = JOY_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = SERENITY_EN;
                        perNum = per * 3;
                    }
                    break;

                case ACCEPTANCE_EN :
                    if(per >= deepHigh) {
                        info = ADMIRATION_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = TRUST_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = ACCEPTANCE_EN;
                        perNum = per * 3;
                    }
                    break;

                case APPREHENSION_EN :
                    if(per >= deepHigh) {
                        info = TERROR_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = FEAR_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = APPREHENSION_EN;
                        perNum = per * 3;
                    }
                    break;

                case DISTRACTION_EN :
                    if(per >= deepHigh) {
                        info = AMAZEMENT_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = SURPRISE_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = DISTRACTION_EN;
                        perNum = per * 3;
                    }
                    break;

                case PENSIVENESS_EN :
                    if(per >= deepHigh) {
                        info = GRIEF_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = SADNESS_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = PENSIVENESS_EN;
                        perNum = per * 3;
                    }
                    break;

                case BOREDOM_EN :
                    if(per >= deepHigh) {
                        info = LOATHING_EN;
                        perNum = (per - 60) * 2.5;
                    } else if(per < deepHigh && per >= deepLow) {
                        info = DISGUST_EN;
                        perNum = (per - 30) * 3;
                    } else {
                        info = BOREDOM_EN;
                        perNum = per * 3;
                    }
                    break;
            }

            space[i].innerHTML = info;
            space[i+2].innerHTML = perNum + " %";
         }

        space = box[1].getElementsByTagName("span");

        for (var i = 0; i < space.length; i = i + 3) {
            
            var emotion = space[i].innerHTML;
            var per = space[i+1].innerHTML.split("%")[0];
            var perNum = 0;

            var info = "";
            
            switch(emotion) {
                case AGGRESSIVENESS_EN :
                    info = AGGRESSIVENESS_EN;
                    perNum = per;
                    break;

                case OPTIMISTIC_EN :
                    info = OPTIMISTIC_EN;
                    perNum = per;
                    break;

                case LOVE_EN :
                    info = LOVE_EN;
                    perNum = per;
                    break;

                case SUBMISSION_EN :
                    info = SUBMISSION_EN;
                    perNum = per;
                    break;

                case AWE_EN :
                    info = AWE_EN;
                    perNum = per;
                    break;

                case DISAPPROVAL_EN :
                    info = DISAPPROVAL_EN;
                    perNum = per;
                    break;

                case REMORSE_EN :
                    info = REMORSE_EN;
                    perNum = per;
                    break;
                    
                case CONTEMPT_EN :
                    info = CONTEMPT_EN;
                    perNum = per;
                    break;
            }

            space[i].innerHTML = info;
            space[i+2].innerHTML = perNum + " %";
         }
        
    }

    setDetailEmotion();
    
    
    function setMainEmotion() {
    	var box = document.getElementsByClassName("emotionBox");
    	var space = box[0].getElementsByTagName("span");

    	var tempEm = space[0].innerHTML;
    	var tempPer = parseInt(space[1].innerHTML.split("%")[0]);
        var tempPerNum = parseInt(space[2].innerHTML.split("%")[0]);

    	for (var i = 3; i < space.length; i = i+3) {
    		if(tempPer < parseInt(space[i+1].innerHTML.split("%")[0])) {
    			tempEm = space[i].innerHTML;
    			tempPer = parseInt(space[i+1].innerHTML.split("%")[0]);
                tempPerNum = parseInt(space[i+2].innerHTML.split("%")[0]);
    		}
    	}

        space = box[1].getElementsByTagName("span");

    	for (var i = 0; i < space.length; i = i+3) {
    		if(tempPer < parseInt(space[i+1].innerHTML.split("%")[0])) {
    			tempEm = space[i].innerHTML;
    			tempPer = parseInt(space[i+1].innerHTML.split("%")[0]);
                tempPerNum = parseInt(space[i+2].innerHTML.split("%")[0]);
    		}
    	}

    	var box = document.getElementsByClassName("horizontalBox");
    	space = box[0].getElementsByTagName("div")[0];
    	space.innerHTML = tempEm;

    	var cColor = "#000000";
    	var tColor = "#000000";
    	var wTextColor = "#000000";
	    var wColor = "#000000";	

    	switch (tempEm) {
    		case ANNOYANCE_EN :
            case ANGER_EN :
            case RAGE_EN :
		    	cColor = "#DD0C81";
		    	tColor = "#DD0C81";
		    	wTextColor = "#EC7ABA";
			    wColor = "#E755A7";	
    			break;
			case INTEREST_EN :
            case ANTICIPATION_EN :
            case VIGILANCE_EN :
		    	cColor = "#F8A631";
		    	tColor = "#F8A631";
		    	wTextColor = "#FCCF81";
			    wColor = "#FCC25E";	
    			break;
			case SERENITY_EN :
            case JOY_EN :
            case ECSTASY_EN :
		    	cColor = "#F3E93F";
		    	tColor = "#F3E93F";
		    	wTextColor = "#F9F487";
			    wColor = "#F7F166";	
    			break;
			case ADMIRATION_EN :
            case TRUST_EN :
            case ACCEPTANCE_EN :
		    	cColor = "#CFDB3C";
		    	tColor = "#CFDB3C";
		    	wTextColor = "#E5EC88";
			    wColor = "#DDE768";	
    			break;

			case APPREHENSION_EN :
            case FEAR_EN :
            case TERROR_EN :
		    	cColor = "#A4CA4A";
		    	tColor = "#A4CA4A";
		    	wTextColor = "#CCE396";
			    wColor = "#BFDB79";	
    			break;
			case DISTRACTION_EN :
            case SURPRISE_EN :
            case AMAZEMENT_EN :
		    	cColor = "#65BFAC";
		    	tColor = "#65BFAC";
		    	wTextColor = "#A8DCBD";
			    wColor = "#91D3AB";	
    			break;
			case PENSIVENESS_EN :
            case SADNESS_EN :
            case GRIEF_EN :
		    	cColor = "#48BEEB";
		    	tColor = "#48BEEB";
		    	wTextColor = "#96DBF5";
			    wColor = "#7AD1F2";	
    			break;
			case BOREDOM_EN :
            case DISGUST_EN :
            case LOATHING_EN :
		    	cColor = "#954395";
		    	tColor = "#954395";
		    	wTextColor = "#C596C6";
			    wColor = "#B67AB6";	
    			break;

			case AGGRESSIVENESS_EN :
		    	cColor = "#D08789";
		    	tColor = "#D08789";
		    	wTextColor = "#E6BDBE";
			    wColor = "#E0ABAC";	
    			break;
			case OPTIMISTIC_EN :
		    	cColor = "#E0B377";
		    	tColor = "#E0B377";
		    	wTextColor = "#EFD6B2";
			    wColor = "#EACB9D";	
    			break;
			case LOVE_EN :
		    	cColor = "#DBCF78";
		    	tColor = "#DBCF78";
		    	wTextColor = "#EBE5B7";
			    wColor = "#E6DEA3";	
    			break;
			case SUBMISSION_EN :
		    	cColor = "#B9C677";
		    	tColor = "#B9C677";
		    	wTextColor = "#D9E0B2";
			    wColor = "#CED89D";	
    			break;

			case AWE_EN :
		    	cColor = "#8FAE7E";
		    	tColor = "#8FAE7E";
		    	wTextColor = "#C1D3B7";
			    wColor = "#B0C7A4";	
    			break;
			case DISAPPROVAL_EN :
		    	cColor = "#79AAA9";
		    	tColor = "#79AAA9";
		    	wTextColor = "#B4D0D0";
			    wColor = "#A0C4C3";	
    			break;
			case REMORSE_EN :
		    	cColor = "#90A1BE";
		    	tColor = "#90A1BE";
		    	wTextColor = "#C2CBDC";
			    wColor = "#B1BDD2";	
    			break;
			case CONTEMPT_EN :
		    	cColor = "#BF81BE";
		    	tColor = "#BF81BE";
		    	wTextColor = "#DCB9D2";
			    wColor = "#D3A6C6";	
    			break;
 
    	}
    	
	    var config1 = liquidFillGaugeDefaultSettings();
	    config1.circleColor = cColor;	//FF7777
	    config1.textColor = tColor;		//FF4444
	    config1.waveTextColor = wTextColor;	//FFAAAA
	    config1.waveColor = wColor;		//FFDDDD
	    config1.circleThickness = 0.1;
	    config1.textVertPosition = 0.5;
	    config1.waveAnimateTime = 1000;
	    var gauge1 = loadLiquidFillGauge("fillgauge1", tempPerNum, config1);

    }

    setMainEmotion();

    function setKoInfo(el) {

    	var check = el.innerHTML;
        var info = "emotion";

    	switch (check) {
    		case ANNOYANCE_EN :
    			info = ANNOYANCE_KO;
    			break;
            case ANGER_EN :
                info = ANGER_KO;
                break;
            case RAGE_EN :
                info = RAGE_KO;
                break;

			case INTEREST_EN :
    			info = INTEREST_KO;
    			break;
            case ANTICIPATION_EN :
                info = ANTICIPATION_KO;
                break;
            case VIGILANCE_EN :
                info = VIGILANCE_KO;
                break;

			case SERENITY_EN :
    			info = SERENITY_KO;
    			break;
            case JOY_EN :
                info = JOY_KO;
                break;
            case ECSTASY_EN :
                info = ECSTASY_KO;
                break;

			case ACCEPTANCE_EN :
    			info = ACCEPTANCE_KO;
    			break;
            case TRUST_EN :
                info = TRUST_KO;
                break;
            case ADMIRATION_EN :
                info = ADMIRATION_KO;
                break;

			case APPREHENSION_EN :
    			info = APPREHENSION_KO;
    			break;
            case FEAR_EN :
                info = FEAR_KO;
                break;
            case TERROR_EN :
                info = TERROR_KO;
                break;

			case DISTRACTION_EN :
    			info = DISTRACTION_KO;
    			break;
            case SURPRISE_EN :
                info = SURPRISE_KO;
                break;
            case AMAZEMENT_EN :
                info = AMAZEMENT_KO;
                break;

			case PENSIVENESS_EN :
    			info = PENSIVENESS_KO;
    			break;
            case SADNESS_EN :
                info = SADNESS_KO;
                break;
            case GRIEF_EN :
                info = GRIEF_KO;
                break;

			case BOREDOM_EN :
    			info = BOREDOM_KO;
    			break;
            case DISGUST_EN :
                info = DISGUST_KO;
                break;
            case LOATHING_EN :
                info = LOATHING_KO;
                break;

			case AGGRESSIVENESS_EN :
    			info = AGGRESSIVENESS_KO;
    			break;
			case OPTIMISTIC_EN :
    			info = OPTIMISTIC_KO;
    			break;
			case LOVE_EN :
    			info = LOVE_KO;
    			break;
			case SUBMISSION_EN :
    			info = SUBMISSION_KO;
    			break;
			case AWE_EN :
    			info = AWE_KO;
    			break;
			case DISAPPROVAL_EN :
    			info = DISAPPROVAL_KO;
    			break;
			case REMORSE_EN :
    			info = REMORSE_KO;
    			break;
			case CONTEMPT_EN :
    			info = CONTEMPT_KO;
    			break;
 
    	}

    	el.innerHTML = info;
    }

    function setEnInfo(el) {

    	var check = el.innerHTML;
    	var info = "emotion";

    	switch (check) {
    		case ANNOYANCE_KO :
    			info = ANNOYANCE_EN;
    			break;
            case ANGER_KO :
                info = ANGER_EN;
                break;
            case RAGE_KO :
                info = RAGE_EN;
                break;

			case INTEREST_KO:
    			info = INTEREST_EN;
    			break;
            case ANTICIPATION_KO :
                info = ANTICIPATION_EN;
                break;
            case VIGILANCE_KO :
                info = VIGILANCE_EN;
                break;

			case SERENITY_KO :
    			info = SERENITY_EN;
    			break;
            case JOY_KO :
                info = JOY_EN;
                break;
            case ECSTASY_KO :
                info = ECSTASY_EN;
                break;

			case ACCEPTANCE_KO :
    			info = ACCEPTANCE_EN;
    			break;
            case TRUST_KO :
                info = TRUST_EN;
                break;
            case ADMIRATION_KO :
                info = ADMIRATION_EN;
                break;

			case APPREHENSION_KO :
    			info = APPREHENSION_EN;
    			break;
            case FEAR_KO :
                info = FEAR_EN;
                break;
            case TERROR_KO :
                info = TERROR_EN;
                break;

			case DISTRACTION_KO :
    			info = DISTRACTION_EN;
    			break;
            case SURPRISE_KO :
                info = SURPRISE_EN;
                break;
            case AMAZEMENT_KO :
                info = AMAZEMENT_EN;
                break;

			case PENSIVENESS_KO :
    			info = PENSIVENESS_EN;
    			break;
            case SADNESS_KO :
                info = SADNESS_EN;
                break;
            case GRIEF_KO :
                info = GRIEF_EN;
                break;

			case BOREDOM_KO :
    			info = BOREDOM_EN;
    			break;
            case DISGUST_KO :
                info = DISGUST_EN;
                break;
            case LOATHING_KO :
                info = LOATHING_EN;
                break;

			case AGGRESSIVENESS_KO :
    			info = AGGRESSIVENESS_EN;
    			break;
			case OPTIMISTIC_KO :
    			info = OPTIMISTIC_EN;
    			break;
			case LOVE_KO :
    			info = LOVE_EN;
    			break;
			case SUBMISSION_KO :
    			info = SUBMISSION_EN;
    			break;
			case AWE_KO :
    			info = AWE_EN;
    			break;
			case DISAPPROVAL_KO :
    			info = DISAPPROVAL_EN;
    			break;
			case REMORSE_KO :
    			info = REMORSE_EN;
    			break;
			case CONTEMPT_KO :
    			info = CONTEMPT_EN;
    			break;
 
    	}

    	el.innerHTML = info;
    }

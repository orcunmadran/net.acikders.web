function jsGrup()
    {
      <!-- CC Lisans URL ve İkonlar -->
      var ccLicense = document.getElementById("license").value;
      switch(ccLicense){
          case "CC 0":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/publicdomain/zero/1.0/deed";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc0.svg?ref=chooser-v1" />'
          break;
          case "CC BY":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" />'
          break;
          case "CC BY-SA":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by-sa/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" />'
          break;
          case "CC BY-NC":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by-nc/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" />'
          break;
          case "CC BY-NC-SA":
          break;
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by-nc-sa/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" />'
          break;
          case "CC BY-ND":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by-nd/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" />'
          break;
          case "CC BY-NC-ND":
          document.getElementById("ccLicenseURL").value = "https://creativecommons.org/licenses/by-nc-nd/4.0/";
          document.getElementById("ccLicenseIcon").value = '<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" />'
      }

      // Multiple Select TYPE
      document.getElementById("type2").value = "";
      var grupType=document.getElementById("type");
      for (var i1 = 0; i1 < grupType.options.length; i1++) {
         if(grupType.options[i1].selected ==true){
              document.getElementById("type2").value += grupType.options[i1].value + ", "
          }
      }

      // Checked Box - Educational Audience
      document.getElementById("educationalAudience2").value = "";
      var eaA=document.getElementById("educationalAudienceA");
      if(eaA.checked == true){
        document.getElementById("educationalAudience2").value += eaA.value + ", "
      }
      var eaB=document.getElementById("educationalAudienceB");
      if(eaB.checked == true){
        document.getElementById("educationalAudience2").value += eaB.value + ", "
      }
      var eaC=document.getElementById("educationalAudienceC");
      if(eaC.checked == true){
        document.getElementById("educationalAudience2").value += eaC.value + ", "
      }
      var eaD=document.getElementById("educationalAudienceD");
      if(eaD.checked == true){
        document.getElementById("educationalAudience2").value += eaD.value + ", "
      }
      var eaE=document.getElementById("educationalAudienceE");
      if(eaE.checked == true){
        document.getElementById("educationalAudience2").value += eaE.value + ", "
      }

      // Checked Box - Educational Use
      document.getElementById("educationalUse2").value = "";
      var euA=document.getElementById("educationalUseA");
      if(euA.checked == true){
        document.getElementById("educationalUse2").value += euA.value + ", "
      }
      var euB=document.getElementById("educationalUseB");
      if(euB.checked == true){
        document.getElementById("educationalUse2").value += euB.value + ", "
      }
      var euC=document.getElementById("educationalUseC");
      if(euC.checked == true){
        document.getElementById("educationalUse2").value += euC.value + ", "
      }
      var euD=document.getElementById("educationalUseD");
      if(euD.checked == true){
        document.getElementById("educationalUse2").value += euD.value + ", "
      }

      // Checked Box - Accesibility Feature
      document.getElementById("accesibilityFeature2").value = "";
      var efA=document.getElementById("accesibilityFeatureA");
      if(efA.checked == true){
        document.getElementById("accesibilityFeature2").value += efA.value + ", "
      }
      var efB=document.getElementById("accesibilityFeatureB");
      if(efB.checked == true){
        document.getElementById("accesibilityFeature2").value += efB.value + ", "
      }
      var efC=document.getElementById("accesibilityFeatureC");
      if(efC.checked == true){
        document.getElementById("accesibilityFeature2").value += efC.value + ", "
      }
      var efD=document.getElementById("accesibilityFeatureD");
      if(efD.checked == true){
        document.getElementById("accesibilityFeature2").value += efD.value + ", "
      }
    }
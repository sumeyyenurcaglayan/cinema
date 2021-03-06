class I18N:
    def __init__(self, language):
        if language == "en":
            self.load_text_in_english()
        elif language == "tr":
            self.load_text_in_turkish()
        else:
            raise NotImplementedError("Unsupported language.")

    def load_text_in_english(self):
        self.emailText = "Enter your E-mail"
        self.passwordText="Enter your password"
        self.title = "My Movie Library"
        self.login="Login"
        self.loginInfoText="Don't have an account? Create a new one!"
        self.homepage="Homepage"

        self.myMovieScores = "My Movie Scores"
        self.didYouWatchTheseMovies = "Did you watch these movies?"
        self.searchMovie = "Search Movie"
        self.search ="Search"
        self.vote="Vote!"
        self.createNewAccount="Create New Account"
        self.userName="Username"
        self.email="E-mail"
        self.password="Password"
        self.passwordControl="Password Control"
        self.recoveryQuestion="Recovery Question"
        self.recoveryQuestionAnswer="Recovery Question Answer"
        self.gender="Gender"
        self.female="Female"
        self.male="Male"

        self.comboquestion1 ="What is your favourite pet?"
        self.comboquestion2 ="What is your favourite color?"
        self.comboquestion3 ="What is the name of favourite teacher?"
        self.comboquestion4 ="What is your lucky number?"
        self.comboquestion5 ="Who is your favourite person?"
        self.comboquestion6 ="Who is your favourite actor/actress? "

        self.createUserInfo1="You have to fill all form elements!"
        self.createUserInfo2 ="Username has empty space!"
        self.createUserInfo3 ="Password and confirmation are different!"
        self.createUserInfo4 ="Username cannot contain empty spaces and special character."
        self.createUserInfo5 ="Password have to contain at least one numerical character."

        self.mainInfo1 = "Acces Denied"
        self.mainInfo2 = "Your E-mail and Password are not matching!"
        self.mainInfo3 = "Wrong E-mail"
        self.mainInfo4 = "Please check your E-mail!"

        self.addNewMovie="Add New Movie"
        self.movieName="Movie Name"
        self.director="Director"
        self.year="Year"
        self.myRating="My Rating"

        self.randomRecommendation="Random Recommendation"

        self.titleDouble = "Double Click To Vote!"
        self. movie="Movie"

        self.img_addMovie = "src_HomePage/AddMovie_en.png"
        self.img_randomMovie="src_HomePage/RandomMovie_en.png"
        self.img_addMov = "src_addMovie/AddMov_en.png"
        self.img_alien = "src_createAccount/alien_en.png"

        self.imgMyMovieLogo="src_main/myMovieLogo_en.png"

        self.imgLogin = "src_main/login_Button_en.png"





    def load_text_in_turkish(self):
        self.emailText = "E-mail adresinizi giriniz"
        self.passwordText ="??ifrenizi giriniz "
        self.title = "Film K??t??phanem"
        self.login = "Giri??"
        self.loginInfoText="Hesab??n yok mu? Yeni hesap yarat! "
        self.homepage="Anasayfa"
        self.myMovieScores="Film Puanlar??m"
        self.didYouWatchTheseMovies="Bu filmleri izledin mi?"
        self.searchMovie="Film Ara"
        self.search="Ara"
        self.vote="Oyla!"
        self.createNewAccount = "Yeni Hesap Olu??tur"
        self.userName = "Kullan??c?? Ad??"
        self.email = "E-mail"
        self.password = "??ifre"
        self.passwordControl = "??ifre Kontrol"
        self.recoveryQuestion = "Kurtarma Sorusu"
        self.recoveryQuestionAnswer = "Kurtarma Sorusu Yan??t??"
        self.gender = "Cinsiyet"
        self.female = "Kad??n"
        self.male = "Erkek"
        self.homepage = "Anasayfa"

        self.comboquestion1="Favori rengin nedir?"
        self.comboquestion2 ="Favori hayvan??n nedir?"
        self.comboquestion3 ="Favori ????retmeninin ad?? nedir?"
        self.comboquestion4 ="??ansl?? numaran nedir?"
        self.comboquestion5 ="En sevdi??in ki??inin ad???"
        self.comboquestion6 ="En sevdi??in oyuncu?"

        self.createUserInfo1 = "B??t??n form bo??luklar??n?? doldurmal??s??n!"
        self.createUserInfo2 = "Kullan??c?? ad?? bo?? olamaz!"
        self.createUserInfo3 = "??ifre ve do??rumalas?? uyu??muyor!"
        self.createUserInfo4 = "Kullan??c?? ad?? bo??luk ve ??zel karakter i??eremez."
        self.createUserInfo5 = "??ifre en az bir tane say??sal karakter i??ermelidir."

        self.mainInfo1= "Giri?? reddedildi"
        self.mainInfo2="E-mail adresiniz ve ??ifreniz uyu??muyor!"
        self.mainInfo3="Yanl???? E-mail"
        self.mainInfo4="L??tfen E-mail adresinizi kontrol edin!"

        self.addNewMovie = "Yeni Film Ekle"
        self.movieName = "Film Ad??"
        self.director = "Y??netmen"
        self.year = "Y??l"
        self.myRating = "Puanlar"

        self.randomRecommendation = "Film ??nerisi"
        self.titleDouble="Oylamak i??in ??ift t??kla!"
        self.movie = "Film"
        self.img_addMovie="src_HomePage/AddMovie_tr.png"
        self.img_randomMovie = "src_HomePage/RandomMovie_tr.png"
        self.img_addMov= "src_addMovie/AddMov_tr.png"
        self.img_alien="src_createAccount/alien_tr.png"

        self.imgMyMovieLogo = "src_main/myMovieLogo_tr.png"

        self.imgLogin= "src_main/login_Button_tr.png"











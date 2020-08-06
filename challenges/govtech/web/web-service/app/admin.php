<?php include 'header.php'; ?>

    <div class="section no-pad-bot" id="index-banner">
        <div class="container">
            <br><br>
            <h1 class="header center gold-text">Restriction</h1>
            <div class="row center">
                <h5 class="header col s12 light">
                    <?php
                    $user_cookie = unserialize(base64_decode($_COOKIE["sectech"]));
                        if ($user_cookie["admin"]) {
                        echo "Good job! Always validate input from external sources and never take it for granted. <br><br>Flag: WH2020{Cook!3Ins3cur3Des3r!al!zat!on_Adm!nR!ghts}";
                    } else {
                        echo "You need to be an admin to view this page.";
                    }
                    ?>
                </h5>

            </div>
            <br><br>
        </div>
    </div>
    <div class="container">
        <div class="section">
            <br><br><br>
            <br><br><br>
            <br><br><br>
            <br><br><br>
        </div>
    </div>
<?php include 'footer.php'; ?>

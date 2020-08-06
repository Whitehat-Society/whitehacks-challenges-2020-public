<?php include 'header.php'; ?>
    <div class="section no-pad-bot" id="index-banner">
        <div class="container">
            <br><br>
            <h1 class="header center gold-text">University Rankings</h1>           
			<h5 class="header center">From time to time, we try to look at SecTech's ranking!</h5>

            <div class="row center">
                <h5 class="header col s12 light">
                </h5>
				<?php
				if (isset($_GET['ranking-url'])) {
					echo file_get_contents($_GET['ranking-url']);
				}			
				?>
				<br><br><br>
				<br><br><br>
				<br><br><br>
				<br><br><br>
            </div>
            <br><br>
        </div>
    </div>
<?php include 'footer.php'; ?>

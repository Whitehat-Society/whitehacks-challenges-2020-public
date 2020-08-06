<?php include 'header.php'; ?>
    <div class="section no-pad-bot" id="index-banner">
        <div class="container">
            <br><br>
            <h1 class="header center gold-text">My Profile</h1>
            <div class="row center">
                <h5 class="header col s12 light">
                </h5>
				<table class="centered">
					  <thead>
					  <tr>
						  <th>Item</th>
						  <th>Value</th>
					  </tr>
					  </thead>

					  <tbody>
   					  <?php 
					  if ($_COOKIE['user_id'] == "c4ca4238a0b923820dcc509a6f75849b") {
					  ?>
					  <tr>
						<td>Name</td>
						<td>Bolo Santosi</td>
					  </tr>
					  <tr>
						<td>Role</td>
						<td><span class="role" data-badge-caption="temp staff">Temp Staff</span></td>
					  </tr>
					  <tr>
						<td>Date of Birth</td>
						<td>1st September 2000</td>
					  </tr>
					  <tr>
						<td>Email</td>
						<td>temp_staff@sectech.com.sg</td>
					  </tr>
					  <?php
					  } else if ($_COOKIE['user_id'] == "c81e728d9d4c2f636f067f89cc14862c") {
					  ?>
					  <tr>
						<td>Name</td>
						<td>Billie Jean</td>
					  </tr>
					  <tr>
						<td>Role</td>
						<td><span class="role" data-badge-caption="perm staff">Perm Staff</span></td>
					  </tr>
					  <tr>
						<td>Date of Birth</td>
						<td>1st July 1988</td>
					  </tr>
					  <tr>
						<td>Email</td>
						<td>billie_jean@sectech.com.sg</td>
					  </tr>
					  <tr>
						<td>Flag</td>
						<td>WH2020{ID0R_D0_N0T_TRUST_US3R_INPUT}</td>
					  </tr>
					  <?php
					  }
					  ?>
					  </tbody>
				</table>
				<br><br><br>
				<br><br><br>
				<br><br><br>
				<br><br><br>
            </div>
            <br><br>
        </div>
    </div>
<?php include 'footer.php'; ?>

<?php include 'header.php'; ?>

    <div class="section no-pad-bot" id="index-banner">
        <div class="container">
            <br><br>
            <h1 class="header center gold-text">View all student grades</h1>
            <br><br>
        </div>
    </div>
<div class="container">
  <div class="section">
      <table>
          <thead>
          <tr>
              <th>Name</th>
              <th>NRIC</th>
              <th>Grades</th>
          </tr>
          </thead>

          <tbody>
          <?php
          //TODO: For future improvements, normalize the schema. This was created unnormalized for rapid prototyping purposes.
          $names=DB::query("SELECT DISTINCT(name), nric from grades");
          if (sizeof($names) > 0) {
              foreach ($names as $name) {
                  echo "<tr>";
                  echo "<td>".$name['name']."</td>";
                  echo "<td>".$name['nric']."</td>";

                  $grades=DB::query("SELECT user_id, course_code, course_name, course_grade from grades WHERE name = %s", $name['name']);
                  if (sizeof($grades) > 0) {
                      ?>
                      <td>
                          <table>
                              <thead>
                              <tr>
                                  <th>Code</th>
                                  <th>Name</th>
                                  <th>Grade</th>
                              </tr>
                              </thead>
                              <tbody>
                              <?php
                                foreach ($grades as $grade) {
                                    ?>
                                    <tr>
                                        <td><?= $grade['course_code'] ?></td>
                                        <td><?= $grade['course_name'] ?></td>
                                        <td><?= $grade['course_grade'] ?></td>
                                    </tr>
                                    <?php
                                }
                              ?>
                              </tbody>
                          </table>
                          <br>
                          <a class='waves-effect waves-light btn' href="./transcript.php?user=temp_acc&password=temp_pass&user_id=<?= $grade['user_id'] ?>&file=transcript.html" target="_blank">View transcript</a>
                          <a class='waves-effect waves-light btn' href="./transcript_write.php?user=temp_acc&password=temp_pass&user_id=<?= $grade['user_id'] ?>&file=transcript-pdf.html&script=js/remove-margins-before-printing.js" target="_blank">Generate transcript</a>
                      </td>
                      <?php
                  }
                  echo "</tr>";
                  ?>
                  <?php

              }
          }
          ?>
          </tbody>
      </table>
  </div>
</div>
<?php include 'footer.php'; ?>
<!DOCTYPE html>
<html>
    <head>
        <title>Start Screen</title>
        <?php include "header.php"; ?>
    </head>
    <body>
        <?php include "nav-top.php"; ?>
        <div class="container-fluid">
            <div class="row">
                <?php include "nav-side.php"; ?>
                <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4">
                    <div id="start-screen" class="card" style='height: 600px'>
                        <h1 id="title">Maze Running Robot</h1>
                        <div id="button">
                            <a href="play-screen.php"><button class="button btnStart">Start Game</button></a>
                            <button class="button btnInfo" data-toggle="modal" data-target="#modalinfo">Instructions</button>
                            <!-- Modal -->
                            <div class="modal fade" id="modalinfo" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                              <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                    <h5 class="modal-title" id="modalTitle">Instructions</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                  </div>
                                  <div class="modal-body">
                                    <p>There will be a maze displayed on the screen and you will need to use the controls to navigate it.</p>
                                    <p>Forward Arrow: Go Forward</p>
                                    <p>Right Arrow: Turn Right</p>
                                    <p>Left Arrow: Turn Left</p>
                                    <p>Back Arrow: Go Backward</p>
                                  </div>
                                </div>
                              </div>
                            </div>
                        </div>
                    </div>               
                </main>
            </div>
        </div>
    </body>
</html>


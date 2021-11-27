<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Title -->
        <title>Administrative Dashboard</title>
        <?php include "header.php"; ?>
    </head>
    <body>
        <?php include "nav-top.php"; ?>
        <div class="container-fluid">
            <div class="row">
                <?php include "nav-side.php"; ?>                
                <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4">
                    <h1>Administrative Panel</h1>
                        <div class="row">
                            <div class="col-sm-6">
                                <div class="card" style='height: 400px'>
                                    <div class="card-body">
                                        <div>
                                            <h4>Sensor Data</h4>
                                        </div> 
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="card" style='height: 400px'>
                                    <div class="card-body">
                                        <div>
                                            <h4>Sensor Data</h4>
                                        </div>                                 
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-4">
                            <div class="col">
                                <div class="card" style='height: 200px'>
                                    <div class="card-body">
                                        <div>
                                            <h4>Car Connection</h4>   
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-4">
                            <div class="col">
                                <div class="card" style='height: 200px'>
                                    <div class="card-body">
                                        <div>
                                            <h4>Current Command History</h4>   
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
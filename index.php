<?php 
if(!session_id()) {
    session_start();
}
$_SESSION['active'] = 0
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>PredictBury</title>

    <!-- Bootstrap Core CSS - Uses Bootswatch Flatly Theme: http://bootswatch.com/flatly/ -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/test.css" rel="stylesheet">

    <script type="text/javascript" src="js/canvasjs.js"></script> 
    <script type="text/javascript" src="js/graph.js"></script>

    <!-- Custom Fonts -->
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body id="page-top" class="index">

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#page-top">PredictBury</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li class="page-scroll">
                        <a href="#portfolio">Portfolio</a>
                    </li>
                    <li class="page-scroll">
                        <a href="#about">About</a>
                    </li>
                    <li class="page-scroll">
                        <a href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <!-- Header -->
   <!--  <header>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <img class="img-responsive" src="img/profile.png" alt="">
                    <div class="intro-text">
                        <span class="name">Purgified</span>
                        <hr class="star-light">
                        <span class="skills">Web Developer - Android Developer - Designer</span>
                    </div>
                </div>
            </div>
        </div>
    </header> -->

    <!-- Portfolio Grid Section -->
    <section id="portfolio" class="all-margin">
        <div class="container">
            <div class="row company-name-margin">
                <div class="col-lg-12 text-center">
                    <form id="the-form" class="form-inline" name="companyBox" method="post">
			            <div class="form-group">
			              <!-- <label for="companyText">Company name</label> -->
			              <input name="company" type="text" size="50" class="form-control" id="companyText" placeholder="Company name">
			            </div>
			            <button type="submit" class="btn btn-default test">Submit</button>
		          </form>
                  <a class="btn btn-danger hidden" id="stop-btn" data-company="">Stop</a>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12 text-center">
                	<div id="chartContainer" style="width:100%; height:350px"></div>  
			          <button class="btn-default" id="addDataPoint">Add DataPoint</button>
	                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="text-center">
        <div class="footer-above">
            <div class="container">
                <div class="row">
                    <div class="footer-col col-md-12 text-center">
                     <!--    <h3>Social Media</h3>
                        <ul class="list-inline">
                            <li>
                                <a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-facebook"></i></a>
                            </li>
                            <li>
                                <a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-google-plus"></i></a>
                            </li>
                            <li>
                                <a href="#" class="btn-social btn-outline"><i class="fa fa-fw fa-twitter"></i></a>
                            </li>
                        </ul> -->
                </div>
            </div>
        </div>
        <div class="footer-below">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        Copyright &copy; PredictBury 2016
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
    <div class="scroll-top page-scroll visible-xs visible-sm">
        <a class="btn btn-primary" href="#page-top">
            <i class="fa fa-chevron-up"></i>
        </a>
    </div>

    

    <!-- jQuery -->
    <script src="js/jquery.js"></script>
    <script
  src="https://code.jquery.com/jquery-1.12.4.min.js"
  integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
  crossorigin="anonymous"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src="js/classie.js"></script>
    <script src="js/cbpAnimatedHeader.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="js/jqBootstrapValidation.js"></script>
    <script src="js/contact_me.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="js/freelancer.js"></script>
    <script>
    $(document).ready(function() {
        // Main array with plot values
        var mainData1 = [
            { y: 10, indexLabel: "Start point" },
            { y:  4 },
            { y: 18 },
            { y:  8 }
        ]

        var mainData2 = [
            { y: 32, indexLabel: "Start point" },
            { y:  8 },
            { y: 10 },
            { y:  25 }
        ]

            var chart = new CanvasJS.Chart("chartContainer", {
                zoomEnabled: false,
                panEnabled: false,
                title: {
                    text: "Adding New DataPoints Dynamically"
                },
                axisX: {
                    title: "Time"
                },
                axisY: {
                    title: "Stock Price"
                },
                data: [
                {
                    type: "spline",
                    dataPoints: mainData1 // Sets data points from plot points
                },
                {
                    type: "spline",
                    dataPoints: mainData2
                }
                ],
                options: {
                    scales: {
                        yAxes: [{
                            stacked: true
                        }]
                    }
                }
            });
            chart.render(); 

            $("#addDataPoint").click(function () {
                var length = chart.options.data[0].dataPoints.length;   
                chart.options.data[0].dataPoints.push({ y: 25 - Math.random() * 10});
                chart.render();
            }); 

        // Adds supplied y-value to the end of the plotted data
        function addYData(yValue) {
            mainData1.push(
                { y: yValue }
            )
            chart.render()
        }

        function addXAndYData(xValue, yValue) {
            mainData1.push(
                { x : xValue},
                { y : yValue}
            )
            chart.render()
        }



        function poll_for_data() {
            $.get('process2.php', function(data) {
                if(JSON.parse(data).text) {
                    data = JSON.parse(data);
                    for(i = 0; i < data.text.length; i++) {
                        // addXAndYData(data.text[i].x, data.text[i].y);
                        addYData(data.text[i].y);
                    }
                }
            });
        };
        setInterval(poll_for_data, 1000);

        $("#the-form").submit(function(e) {
            e.preventDefault();
            $("#stop-btn").removeClass('hidden');
            $("#stop-btn").attr('data-company', $("#companyText").val());
            $.post('process.php', {'company': $("#companyText").val()});
        });

        $("#stop-btn").click(function(e) {
            $(this).addClass('hidden');
            $.post('process.php', {'stop': $(this).attr('data-company')});
            $(this).attr('data-company', '');
        });
    });
    </script>
</body>

</html>
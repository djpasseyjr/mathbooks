<html>
<head>
<title>Portal to MathBooks</title>

<link rel="stylesheet" type="text/css" href="mathbooks/static/header_styles.css">


<div class="header">

    <div class="nav">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/checkout">Checkout</a></li>
        <li><a href="/checkin">Return</a></li>
        <li><a href="/admin">Tools</a></li>
    </ul>
    </div>

      <div class="logo"><a href="/">
      <img src="mathbooks/static/images/byulogo.png" sizes="(max-width: 709px) 85vw, (max-width: 909px) 81vw, (max-width: 1362px) 88vw, 1200px" width="405" height="30" style="margin-top:8px;margin-left:5px;"alt="Mathematics Department">
      </a></div>
</div>

<div class="bod">
Password please...
<?php 
   $changed = chdir("/Library/WebServer/Documents/mathbooks");
   $dir = shell_exec("ls");
   $loc = shell_exec("/usr/local/bin/python bin/app.py > mathbooks.log 2>&1 &");
   echo($loc);
?>

<!-- meta HTTP-EQUIV="REFRESH" content="5; url=http://0.0.0.0:8080" /-->
</div>

<div class="footer">
BYU Department of Mathematics 2017
</div>

</html>


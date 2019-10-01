<?php
class permissions
{
  public $username = "admin";
  public $password = "password";
  function __construct($password)
  {
    $this->password = $password;
  }
}
$k = new permissions($argv[1]);
echo urlencode(base64_encode(serialize($k)));
echo "\n";
//echo $argv[1];
?>

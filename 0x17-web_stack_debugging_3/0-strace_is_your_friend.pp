exec { 'fix-wordpress':
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => '/bin',
}

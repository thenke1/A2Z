#!/usr/bin/perl -w

#	Name	:Trudi Henke
#	Class	:1300-001
#	Assign#	:17
#	Due	:Dec. 14, 2011

#	Honor Pledge: On my honor as a student of the University
#	   of Nebraska at Omaha, I have neither given nor
#	   received unauthorized help on this homework
#	   assignment.

#	NAME:  Trudi Henke
#	NUID:  598
#	EMAIL: thenke@unomaha.edu

#	Partners: None

#	A page for contacting A2Z Roofing.

use strict;
use CGI qw /:standard/;
#use CGI::Carp qw/fatalsToBrowser/;
print header ();
print start_html(-title=>'Results of CGI script');
my ($roofyears, $servicetime, $sqft, $hearabout, $namefirst, $namelast, $address, $city, $state, $zipcode, $phonenum, $email, $comment);

$roofyears = param ('roof_years');
$servicetime = param('service_time');
$sqft = param('sq_ft');
$hearabout = param('hear_about');
$namefirst =  param('name_first');
$namelast = param('name_last');
$address = param('address');
$city = param('city');
$state = param('State');
$zipcode = param('Zip_code');
$phonenum = param('Phone_num');
$email = param('email');
$comment = param('comment');

if ($namefirst ne '' && $namelast ne '' && $address ne '' && $city ne '' && $state ne '' && $zipcode ne '' && $phonenum ne '' && $email ne '')
{
	use Mail::Sendmail;
	my $mailTo = 'thenke_mayhew@yahoo.com';
	my $mailFrom = $email;
	my $subjectLine = 'QUOTE';
	my $message = $roofyears.$servicetime.$sqft.$hearabout.$namefirst.$namelast.$address.$city.$state.$zipcode.$phonenum.$email.$comment;
	my %mail = ("To" => $mailTo, "From" => $mailFrom, "Subject" => $subjectLine, "Message" => $message, 'Content-Type' => 'text/plain');

	print p(h1("Your information has been sent and you should be contacted within the next 48 hours, Thank you!"));
}

else
{
	if ($namefirst eq '') # if any of the fields are empty 
	{
		print p(b({-style=>'Color: red;'}, "Please enter a first name, Thank you!"));
	}
	if ($namelast eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter a last name, Thank you!"));
	}
	if ($address eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter an addess, Thank you!"));
	}
	if ($city eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter a City, Thank you!"));
	}
	if ($state eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter a State, Thank you!"));
	}
	if ($zipcode eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter a Zip code, Thank you!"));
	}
	if ($phonenum eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter a phone number, Thank you!"));
	}
	if ($email eq '')
	{
		print p(b({-style=>'Color: red;'}, "Please enter an E-mail address, Thank you!"));
	}
	print p(a({-href=>"http://blizzard.ist.unomaha.edu/~thenke/project/quote.html", -style=>'Color: blue;'}, "Go back and fill in the field(s)!"));
}
print p(a({-href=>"http://jigsaw.w3.org/css-validator/check/referer"}, img({-style=>'width: 88px; height: 31px;', -src=>"http://jigsaw.w3.org/css-validator/images/vcss", -alt=>"Valid CSS!"})));
print p(a({-href=>"http://validator.w3.org/check?uri=referer"}, img({-src=>"http://www.w3.org/Icons/valid-xhtml10", -alt=>"Valid XHTML 1.0 Transitional", -style=>'height: 31px; width: 88px;'})));

print end_html();

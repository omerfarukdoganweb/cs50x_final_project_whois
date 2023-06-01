# cs50x_final_project_whois
#### Video Demo:  (https://youtu.be/hTzLHuzLyjA)


WHOIS Query using Python
You can use the following Python code to query the DNS registration information of a given URL. This code connects to various WHOIS servers to obtain information such as the owner of a domain, registration date, last updated date and expiration date.

Usage
Enter the website address for which you want to perform a WHOIS query on the url variable.
Run the code.

<code>python
$ python whois.py
Enter website url for whois query: www.example.com
</code>
  
Dependencies
This code requires the socket library to function.

Example Output
The following example shows the output from a WHOIS query performed on google.com.

<code>Registrant Name: DNS Admin
Registrant Organization: Google Inc.
Registrant Street: 1600 Amphitheatre Parkway
Registrant City: Mountain View
Registrant State/Province: CA
Registrant Postal Code: 94043
Registrant Country: US
Registrant Phone: +1.6502530000
Registrant Phone Ext:
Registrant Fax: +1.6506188571
Registrant Fax Ext:
Registrant Email: dns-admin@google.com
Registry Admin ID: Not Available From Registry
Admin Name: Domain Admin
Admin Organization: Google Inc.
Admin Street: Please contact contact-admin@google.com, 1600 Amphitheatre Parkway
Admin City: Mountain View
Admin State/Province: CA
Admin Postal Code: 94043
Admin Country: US
Admin Phone: +1.6502530000
Admin Phone Ext:
Admin Fax: +1.6506188571
Admin Fax Ext:
Admin Email: domain-admin@google.com
Registry Tech ID: Not Available From Registry
Tech Name: DNS Admin
Tech Organization: Google Inc.
Tech Street: 2400 E. Bayshore Pkwy
Tech City: Mountain View
Tech State/Province: CA
Tech Postal Code: 94043
Tech Country: US
Tech Phone: +1.6503300100
Tech Phone Ext:
Tech Fax: +1.6506181499
Tech Fax Ext:
Tech Email: dns-admin@google.com
Name Server: ns1.google.com
Name Server: ns2.google.com
Name Server: ns3.google.com
Name Server: ns4.google.com
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2023-06-01T00:00:00Z <<<
</code>
License
This project is licensed under the MIT License.

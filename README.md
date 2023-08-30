# Computer-Security-mini-project
<p>Run from Security.py</p>

## This is a simple program that implements 3 ciphering techniques:
<ul>
<li>Single DES</li>
<li>Triple DES</li>
<li>RSA</li>
</ul>
The program is written in Python and executed in a CLI terminal; the user starts by selecting a ciphering technique from the available choices by entering the number of the corresponding algorithm in the enumeration, then they are prompted to enter a text message (which can include any character that uses ascii encoding) to be encrypted with the chosen algorithm, the program then proceeds to encrypt the message and decrypt it back to plaintext form and displaying the results on screen.
The user is then free to decide whether to continue with another algorithm or exit the program. The program exits when the user enters anything but “Yes”/”yes”/”y”/”Y” in the continue dialogue.

## Libraries used:
<ul>
<li>rsa (RSA encryption using private key and public key)</li>
<li>pycryptodome</li>
  <ul><li>Crypto.Cipher</li>
    <ul><li>DES (Single DES encryption)</li>
	      <li>DES3 (Triple DES encryption)</li></ul></ul>
  <ul><li>Crypto.Random</li>
	  <ul><li>get_random_bytes (for key gen in DES3)</li></ul></ul>
  <ul><li>secrets</li>
    <ul><li>token_bytes (for key gen in DES)</li></ul>
</ul>

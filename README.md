# Cryptography

## Caesar Cipher


This is a very basic cipher whose first recorder use was in Rome by Julius Caesar whom the cipher is named after. It is one of the simplest cryptographic techniques and is an example of a substitution cipher. Each letter in the plaintext message is replaced by a letter in the alphabet a predetermined number of places along. To decrypt the reserve of each shift is taken. For example, to encrypt a plaintext message ‘hello’ with a shift of 5, h would become m, e would become j and so on till you get an encrypted message of mjqqt. While the Caesar is easy to use and understand it is also very easy to crack as there is only 25 possible encryptions and is therefore very susceptible to brute forcing.

Cracking a Caesar cipher is very easy. Given there are only 25 possible encryptions you simply go through and try each of the keys until a result is obtained that is an understandable message. A possible way to increase the complexity to avoid this simple decryption method would be to perform two shifts however this does not work as performing a shift of 5 then a shift of 3 is simply equal to performing a shift of 8. Another method of increasing complexity would be to translate your message to a different language first then perform the substitutions so that when decrypted the foreign language could blend in with the other ‘gibberish’. This however relies on the intended receiver being fluent in the chosen language and that the interceptor doesn’t speak the chosen language.

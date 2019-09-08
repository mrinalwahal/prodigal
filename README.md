## Prodigal Tech - Assignment

### Table of Contents:
  - [Usage](#usage)
  - [Changes In Output](#changes)
  - [What can be improved?](#improvements)
  - [Difficulties Encountered](#difficulties)

<a name="usage">

#### Usage

Though the `flask` API is deployed at [wahal.pythonanywhere.com](https://wahal.pythonanywhere.com), `pymongo` has been experiencing trouble in connecting to the DB due to some interference by WSGI apps whilst initialising the server.

Therefore, I've added a `manual_tests.py` file in the codebase, which can easily be executed to test all the coded functions being called for testing all the endpoints.

<a name="changes">

#### Changes in Output

Since the file `manual_tests.py` only calls the functions for testing the code, the final output may not be in the exact format specified by the assignment doc.

However, the calculated information by the functions should be correct. Therefore, you may not see the metadata info like `student_id` or `class_id` appearing in the output from `manual_tests.py` file. This is because this extra metadata is returned in responses from the Flask API. Reading that code would clarify this for you.

<a name="improvements">

#### Improvements Suggested

In a lot of cases the required output format of the result forces the coder to process already available data in fancy fashions simply to present the data in required format. Example - When the result contains a field `score`, the output format mentioned in the assingment doc wants the same score value with the key `marks`. And therefore, uneccessary processing increases execution time.

In an ideal environment, the API's job should be to solely return the fetched or calculated data. And the front-end (receiving) client must do the job of processing retrieved data to present it in any fancy fashion required.

<a name="difficulties">

#### Difficulties Envountered during dev

For some reason Flask's interaction with Pymongo is super slow and even the C++ binaries which existed earlier are now no longer available to spoeed up the execution - or perhaps, I couldn't find them.

Since pymongo is calling the MongoDB server to process every request, the response time is quite slow. And I'm unsure whether I'm not doing something that's required to speed up the process or its a thing from the hosted AWS server itself.

This is also the reason, that if the flask server runs just fine at the deployed URI ([wahal.pythonanywhere.com](https://wahal.pythonanywhere.com)), numerous endpoints do not return the calculated values. Could be due to timeouts from the server. Or something else.

Therefore, I suggest using the `manual_tests.py` file which works fine.

<br>

**Thanks, Prodigal Tech! It was an interesting assignment. See ya! :)**
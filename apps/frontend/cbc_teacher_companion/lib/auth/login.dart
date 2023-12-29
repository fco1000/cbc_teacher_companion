import 'package:flutter/material.dart';
import 'package:local_auth/local_auth.dart';
import 'package:cbc_teacher_companion/main.dart';

class LoginScreen extends StatelessWidget {
  final LocalAuthentication localAuth = LocalAuthentication();

  LoginScreen({Key? key}) : super(key: key);

  // This widget is the root of your application.
  

  Future<void> _authenticateWithBiometrics(BuildContext context) async {
    final isAuthenticated = await localAuth.authenticate(
        localizedReason: 'Login to access your account');

    if (isAuthenticated) {
      // ignore: use_build_context_synchronously
      Navigator.of(context).push(
        MaterialPageRoute(
          builder: (context) =>
              const MyHomePage(title: 'CBC Teacher Assistant'),
        ),
      );
    }
  }

  Future<void> _login(BuildContext context) async {
    Navigator.of(context).push(MaterialPageRoute(
        builder: (context) =>
            const MyHomePage(title: 'CBC Teacher Assistant')));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Login'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => _login(context),
              child: const Text('Login'),
            ),
            ElevatedButton(
              onPressed: () => _authenticateWithBiometrics(context),
              child: const Text('Biometrics Login'),
            ),
          ],
        ),
      ),
    );
  }
}

// class LoginScreen extends StatefulWidget {
//   const LoginScreen({Key? key, required this.title}) : super(key: key);

//   final String title;

//   @override
//   State<LoginScreen> createState() => _LoginScreenState();
// }

// class _LoginScreenState extends State<LoginScreen> {
//   late final LocalAuthentication auth;
//   bool _supportState = false;

//   @override
//   void initState() {
//     super.initState();
//     auth = LocalAuthentication();
//     auth.isDeviceSupported().then((bool isSupported) => setState(() {
//           _supportState = isSupported;
//         }));
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text(widget.title),
//         backgroundColor: Theme.of(context).colorScheme.inversePrimary,
//       ),
//       body: Column(
//         mainAxisAlignment: MainAxisAlignment.center,
//         children: <Widget>[
//           ElevatedButton(
//               onPressed: _authenticate, child: const Text('Authenticate'))
//         ],
//       ),
//     );
//   }

//   Future<void> _authenticate() async {
//       bool authenticated = await auth.authenticate(
//           localizedReason: 'This is to verify that an authorized user is currently logging in',
//           options: const AuthenticationOptions(
//               stickyAuth: true, biometricOnly: false));
//       print('authenticated: $authenticated');
      
//   }
// }

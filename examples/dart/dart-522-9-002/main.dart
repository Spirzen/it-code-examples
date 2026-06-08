
import 'dart:convert';
import 'dart:io';

Future<void> fetchExample() async {
  final client = HttpClient();
  try {
    final request = await client.getUrl(Uri.parse('https://httpbin.org/get'));
    final response = await request.close();
    if (response.statusCode != 200) {
      throw HttpException('код ${response.statusCode}');
    }
    final body = await response.transform(utf8.decoder).join();
    final data = jsonDecode(body) as Map<String, dynamic>;
    print(data['origin']);
  } finally {
    client.close(force: true);
  }
}

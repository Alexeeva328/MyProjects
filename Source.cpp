#define _WINSOCK_DEPRECATED_NO_WARNINGS
#include <stdio.h>
#include <winsock2.h> // Wincosk2.h должен быть раньше windows!
#include <windows.h>
#include <locale.h>
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
#include <string>
#include <stdlib.h>




#pragma comment(lib,"wsock32.lib")
#define _CRT_SECURE_NO_WARNINGS
using namespace std;
using namespace rapidjson;

int main()
{
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2, 2);
	WSAStartup(wVersionRequested, &wsaData);

	for (;;)
	{
		cout <<"Input any symbol and click Enter: " << endl;
		if (getchar())
		{
			int rc;
			int sizePack;
			SOCKET s1 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

			hostent* IpServer;
			char* localIP;
			IpServer = gethostbyname("pi");
			localIP = inet_ntoa(*(struct in_addr *)*IpServer->h_addr_list);


			struct sockaddr_in anAddr;
			anAddr.sin_family = AF_INET;
			anAddr.sin_port = htons(9000);
			anAddr.sin_addr.S_un.S_addr = inet_addr(localIP);

			rc = connect(s1, (struct sockaddr*) & anAddr, sizeof(struct sockaddr));

			// create object from string literal
		/*	string jsonSTR = "{ \"happy\": true, \"pi\": 3.141 }";
			Document doc;
			doc.Parse(jsonSTR.c_str());
			Value& val = doc["pi"];
			val.SetInt(val.GetDouble() + 3.1);//кажется,что здесь в 16-тиричной системе счисления число прибавляется

			StringBuffer buffer;
			Writer<StringBuffer> writer(buffer);
			doc.Accept(writer);

			cout << "buf = " << buffer.GetString() << endl;
			*/

			/*char jsonChar[35];
			for (int i = 0; i <= jsonSTR.length(); i++)
			{
				if (jsonSTR[i] == 'М')
					jsonChar[i] = ' ';
				else
					jsonChar[i] = jsonSTR[i];
			}
			for (int i = 0; i <= sizeof(jsonChar); i++)
			{
				if (jsonChar[i] == 'М')
					jsonChar[i] = ' ';
			}
			char sizeHeader[4] = { 22 }; //размер заголовка
			sizePack = send(s1, sizeHeader, sizeof(sizeHeader), 0);
			rc = send(s1, jsonChar, sizeof(jsonChar), 0);*/
			//cout << str << endl;
			char str[1];
			str[0] = 'g';
			rc = send(s1, str, sizeof(str), 0);
			cout << str[0] << endl;
			char answerFromPi[15];
			
			//char *p_answer = new char[str[0]];
			
			//rc = recv(s1, p_answer, sizeof(p_answer), 0);
			//cout << p_answer << endl;
			rc = recv(s1, answerFromPi, sizeof(answerFromPi), 0);

			
			if (answerFromPi[0] == '1' && answerFromPi[1] == '0')
			{
				char *lenImage = new char[5];
				for (int i = 0; i < 5; i++)
				{
					lenImage[i] = answerFromPi[i + 7];
				}
				str[0] = '1'; //true = 1 ; false = 0
				rc = send(s1, str, sizeof(str), 0);

				long sizeIm = atol(lenImage);
				char *dataImage = new char[sizeIm+10];
				rc = recv(s1, dataImage, sizeIm + 10, 0);

				//}
				/*for (int i = 0; i <= sizeof(answerFromPi); i++)
				{
					if (answerFromPi[i] == 'М')
						answerFromPi[i] = ' ';
				}*/
				//string data = new string[answerFromP];
				cout << dataImage << endl;
				//delete[] p_answer;
				delete[] lenImage;
			}
			closesocket(s1);
		}
	}
	WSACleanup();
	system("pause");
	return 0;
}
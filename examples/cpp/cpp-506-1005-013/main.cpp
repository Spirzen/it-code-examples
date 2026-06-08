#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

#ifdef _WIN32
#include <tlhelp32.h>
#else
#include <dirent.h>
#include <unistd.h>
#endif

class ProcessViewer {
public:
    static void listProcesses() {
        #ifdef _WIN32
        HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if (hSnapshot == INVALID_HANDLE_VALUE) return;

        PROCESSENTRY32 pe32;
        pe32.dwSize = sizeof(PROCESSENTRY32);

        if (Process32First(hSnapshot, &pe32)) {
            do {
                std::cout << "PID: " << pe32.th32ProcessID 
                          << " | Name: " << pe32.szExeFile << std::endl;
            } while (Process32Next(hSnapshot, &pe32));
        }
        CloseHandle(hSnapshot);
        #else
        DIR* dir;
        struct dirent* ent;
        if ((dir = opendir("/proc")) != NULL) {
            while ((ent = readdir(dir)) != NULL) {
                if (isdigit(ent->d_name[0])) {
                    std::string pid = ent->d_name;
                    std::string statPath = "/proc/" + pid + "/stat";
                    std::ifstream statFile(statPath);
                    
                    if (statFile.is_open()) {
                        std::string name;
                        statFile >> name; // PID
                        statFile >> name; // Comm (имя процесса в скобках)
                        
                        // Удаляем скобки из имени
                        name.erase(std::remove(name.begin(), name.end(), '('), name.end());
                        name.erase(std::remove(name.begin(), name.end(), ')'), name.end());
                        
                        std::cout << "PID: " << pid << " | Name: " << name << std::endl;
                        statFile.close();
                    }
                }
            }
            closedir(dir);
        }
        #endif
    }
};

int main() {
    std::cout << "Список запущенных процессов:" << std::endl;
    ProcessViewer::listProcesses();
    return 0;
}

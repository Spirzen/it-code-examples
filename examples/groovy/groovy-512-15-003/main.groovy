class Person {
    void introduce() {
        println "I am a person"
    }
}

class Student extends Person {
    @Override
    void introduce() {
        println "I am a student"
    }
}

def people = [new Person(), new Student()]
people.each { it.introduce() }

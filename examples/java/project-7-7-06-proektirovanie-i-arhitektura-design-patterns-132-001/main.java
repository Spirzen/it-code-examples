import java.util.ArrayList;
import java.util.List;

interface OrganizationUnit {
    String getName();
    long getSalary();
}

class Employee implements OrganizationUnit {
    private final String name;
    private final long salary;

    Employee(String name, long salary) {
        this.name = name;
        this.salary = salary;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public long getSalary() {
        return salary;
    }
}

class Department implements OrganizationUnit {
    private final String name;
    private final List<OrganizationUnit> units = new ArrayList<>();

    Department(String name) {
        this.name = name;
    }

    void add(OrganizationUnit unit) {
        units.add(unit);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public long getSalary() {
        return units.stream().mapToLong(OrganizationUnit::getSalary).sum();
    }
}

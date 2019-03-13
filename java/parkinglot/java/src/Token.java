import java.sql.Time;
import java.util.Date;

public class Token {
    StringBuffer tokenNumber;
    Time entryTime;
    Time exitTime;
    Float charge;
    public String calculateDuration() {
        Time diff = entryTime.getTime() - exitTime.getTime();
        return diff;
    }
    public float calculateCharge(Time diff) {
        float dayCharge = 10;
        float hourCharge = 2;
        int days = strip(diff, days);
        float hours = strip(diff, hours);
        float charge = days*dayCharge + hours*hourCharge;
        return charge;
    }
}
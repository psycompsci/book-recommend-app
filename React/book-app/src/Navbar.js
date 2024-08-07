export default function Navbar() {
    return (
        <nav className="nav">
            <a href="/" className="site-title">Book App</a>
            <ul>
                <li>
                    <a href="/signin">SignIn</a>           
                </li>
            </ul>
        </nav>
    );
}
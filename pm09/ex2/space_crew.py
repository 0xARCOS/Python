from enum import Enum
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self):
        # Mission ID debe empezar con "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Al menos un Commander o Captain
        leadership_ranks = {Rank.commander, Rank.captain}
        if not any(member.rank in leadership_ranks for member in self.crew):
            raise ValueError("Mission must have at least one \
            Commander or Captain")

        # Todos los miembros deben estar activos
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        # Misiones largas necesitan 50% con experiencia
        if self.duration_days > 365:
            experienced = (
                sum(1 for member in self.crew if member.years_experience >= 5)
            )
            if experienced / len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need \
                50% experienced crew (5+ years)")

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 41)

    # Tripulación válida
    crew = [
        CrewMember(
            member_id="CMD001",
            name="Sarah Connor",
            rank="commander",
            age=42,
            specialization="Mission Command",
            years_experience=15,
            is_active=True,
        ),
        CrewMember(
            member_id="LTN002",
            name="John Smith",
            rank="lieutenant",
            age=35,
            specialization="Navigation",
            years_experience=8,
            is_active=True,
        ),
        CrewMember(
            member_id="OFF003",
            name="Alice Johnson",
            rank="officer",
            age=28,
            specialization="Engineering",
            years_experience=4,
            is_active=True,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 6, 1),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("=" * 41)

    print("\nExpected validation error:")
    try:
        invalid_crew = [
            CrewMember(
                member_id="OFF001",
                name="Test Officer",
                rank="officer",
                age=30,
                specialization="Test",
                years_experience=2,
            )
        ]
        SpaceMission(
            mission_id="TEST01",  # No empieza con "M"
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=invalid_crew,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()

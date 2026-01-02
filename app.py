#!/usr/bin/env python3
"""
Christmas Sunday Finder - Advanced Python Implementation
Finds all years where December 25th falls on a Sunday within a given range.

Author: Advanced Python Developer
Date: 2024
Version: 3.0
"""

import datetime
import calendar
from typing import List, Dict, Optional, Tuple
import json
import csv
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd

class ChristmasSundayFinder:
    """
    Advanced Christmas Sunday finder with multiple algorithms and analysis tools.
    """
    
    def __init__(self):
        self.cache = {}
        self.statistics = {}
        
    def find_xmas_sunday_basic(self, start_year: int, end_year: int) -> List[int]:
        """
        Basic implementation using datetime module.
        
        Args:
            start_year: Starting year (inclusive)
            end_year: Ending year (inclusive)
            
        Returns:
            List of years where Dec 25 falls on Sunday
            
        Time Complexity: O(n) where n is the number of years
        Space Complexity: O(k) where k is the number of Sunday Christmases
        """
        if not isinstance(start_year, int) or not isinstance(end_year, int):
            raise TypeError("Years must be integers")
        
        if start_year > end_year:
            raise ValueError("Start year must be <= end year")
        
        if start_year < 1 or end_year > 9999:
            raise ValueError("Years must be between 1 and 9999")
        
        sunday_years = []
        
        for year in range(start_year, end_year + 1):
            # December 25, month=12, day=25
            date = datetime.date(year, 12, 25)
            if date.weekday() == 6:  # Sunday is 6 in datetime (Monday=0)
                sunday_years.append(year)
                
        return sunday_years
    
    def find_xmas_sunday_calendar(self, start_year: int, end_year: int) -> List[int]:
        """
        Alternative implementation using calendar module.
        
        Args:
            start_year: Starting year (inclusive)
            end_year: Ending year (inclusive)
            
        Returns:
            List of years where Dec 25 falls on Sunday
        """
        sunday_years = []
        
        for year in range(start_year, end_year + 1):
            # calendar.weekday returns Monday=0, Sunday=6
            if calendar.weekday(year, 12, 25) == 6:
                sunday_years.append(year)
                
        return sunday_years
    
    def find_xmas_sunday_optimized(self, start_year: int, end_year: int) -> List[int]:
        """
        Optimized implementation using mathematical patterns.
        
        Uses the fact that the calendar repeats every 28 years in the Gregorian calendar
        (except for century years not divisible by 400).
        
        Args:
            start_year: Starting year (inclusive)
            end_year: Ending year (inclusive)
            
        Returns:
            List of years where Dec 25 falls on Sunday
        """
        cache_key = f"{start_year}_{end_year}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Base pattern for a 28-year cycle (2000-2027)
        base_pattern = [2000, 2005, 2011, 2016, 2022]
        
        sunday_years = []
        
        # Calculate for the first 28-year cycle
        first_cycle_start = (start_year // 28) * 28
        first_cycle_end = first_cycle_start + 27
        
        for year in range(max(start_year, first_cycle_start), 
                         min(end_year, first_cycle_end) + 1):
            # Check if this year matches the pattern
            offset = year - first_cycle_start
            if offset % 28 in [year - first_cycle_start for year in base_pattern]:
                # Verify with actual calculation (leap year adjustments)
                if datetime.date(year, 12, 25).weekday() == 6:
                    sunday_years.append(year)
        
        # Extend the pattern for full range
        current_cycle_start = first_cycle_start
        while current_cycle_start <= end_year:
            for base_year in base_pattern:
                target_year = current_cycle_start + (base_year - 2000)
                if start_year <= target_year <= end_year:
                    # Verify the calculation
                    if datetime.date(target_year, 12, 25).weekday() == 6:
                        if target_year not in sunday_years:
                            sunday_years.append(target_year)
            current_cycle_start += 28
        
        # Handle century years (they break the 28-year cycle)
        century_year = ((start_year // 100) + 1) * 100
        if century_year <= end_year and century_year % 400 != 0:
            # Century years not divisible by 400 don't have Sunday Christmas
            # if they would have according to the pattern
            sunday_years = [year for year in sunday_years if year != century_year]
        
        result = sorted(list(set(sunday_years)))
        self.cache[cache_key] = result
        return result
    
    def find_xmas_sunday_generator(self, start_year: int, end_year: int):
        """
        Generator version for memory-efficient processing of large ranges.
        
        Args:
            start_year: Starting year (inclusive)
            end_year: Ending year (inclusive)
            
        Yields:
            Years where Dec 25 falls on Sunday
        """
        for year in range(start_year, end_year + 1):
            if datetime.date(year, 12, 25).weekday() == 6:
                yield year
    
    def analyze_patterns(self, start_year: int, end_year: int) -> Dict:
        """
        Analyze patterns in Christmas Sunday occurrences.
        
        Args:
            start_year: Starting year for analysis
            end_year: Ending year for analysis
            
        Returns:
            Dictionary containing various statistics and patterns
        """
        years = self.find_xmas_sunday_optimized(start_year, end_year)
        
        if not years:
            return {"error": "No Sunday Christmases found in range"}
        
        # Calculate gaps between occurrences
        gaps = [years[i+1] - years[i] for i in range(len(years)-1)]
        
        # Calculate decades distribution
        decades = Counter((year // 10) * 10 for year in years)
        
        # Calculate centuries distribution
        centuries = Counter((year // 100) for year in years)
        
        # Find longest gap
        max_gap = max(gaps) if gaps else 0
        max_gap_index = gaps.index(max_gap) if gaps else 0
        
        # Find most common gap
        gap_counts = Counter(gaps)
        most_common_gap = gap_counts.most_common(1)[0] if gap_counts else (0, 0)
        
        # Calculate frequency
        total_years = end_year - start_year + 1
        frequency = len(years) / total_years
        
        analysis = {
            "total_sunday_christmases": len(years),
            "frequency_percentage": round(frequency * 100, 2),
            "years_list": years,
            "gaps": gaps,
            "average_gap": round(sum(gaps) / len(gaps), 2) if gaps else 0,
            "max_gap": max_gap,
            "max_gap_years": (years[max_gap_index], years[max_gap_index + 1]) if max_gap > 0 else None,
            "most_common_gap": most_common_gap[0],
            "most_common_gap_frequency": most_common_gap[1],
            "decades_distribution": dict(decades),
            "centuries_distribution": dict(centuries),
            "first_occurrence": years[0],
            "last_occurrence": years[-1],
            "next_occurrence_from_now": self._find_next_occurrence(years)
        }
        
        self.statistics = analysis
        return analysis
    
    def _find_next_occurrence(self, years: List[int]) -> Optional[int]:
        """Find the next Sunday Christmas from current year."""
        current_year = datetime.date.today().year
        for year in years:
            if year >= current_year:
                return year
        return None
    
    def visualize_data(self, start_year: int, end_year: int, save_path: str = None):
        """
        Create visualizations of Christmas Sunday patterns.
        
        Args:
            start_year: Starting year for analysis
            end_year: Ending year for analysis
            save_path: Optional path to save the visualization
        """
        try:
            analysis = self.analyze_patterns(start_year, end_year)
            years = analysis['years_list']
            
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
            fig.suptitle(f'Christmas Sunday Analysis ({start_year}-{end_year})', fontsize=16)
            
            # 1. Timeline of Sunday Christmases
            ax1.scatter(years, [1]*len(years), alpha=0.7, s=50, c='red')
            ax1.set_title('Timeline of Sunday Christmases')
            ax1.set_xlabel('Year')
            ax1.set_ylabel('')
            ax1.set_yticks([])
            ax1.grid(True, alpha=0.3)
            
            # 2. Gap distribution
            if analysis['gaps']:
                ax2.hist(analysis['gaps'], bins=20, alpha=0.7, color='green', edgecolor='black')
                ax2.set_title('Distribution of Gaps Between Sunday Christmases')
                ax2.set_xlabel('Gap (years)')
                ax2.set_ylabel('Frequency')
                ax2.axvline(analysis['average_gap'], color='red', linestyle='--', 
                           label=f'Average: {analysis["average_gap"]}')
                ax2.legend()
            
            # 3. Decade distribution
            decades = list(analysis['decades_distribution'].keys())
            decade_counts = list(analysis['decades_distribution'].values())
            ax3.bar([f"{d}s" for d in decades], decade_counts, alpha=0.7, color='gold')
            ax3.set_title('Sunday Christmases by Decade')
            ax3.set_xlabel('Decade')
            ax3.set_ylabel('Count')
            ax3.tick_params(axis='x', rotation=45)
            
            # 4. Frequency over time (moving window)
            window_size = max(28, len(years) // 10)
            frequencies = []
            window_centers = []
            
            for i in range(window_size, len(years)):
                start = years[i-window_size]
                end = years[i]
                window_years = end - start + 1
                freq = window_size / window_years * 100
                frequencies.append(freq)
                window_centers.append((start + end) // 2)
            
            if frequencies:
                ax4.plot(window_centers, frequencies, marker='o', linewidth=2)
                ax4.set_title(f'Frequency Trend (Moving {window_size}-year window)')
                ax4.set_xlabel('Year')
                ax4.set_ylabel('Frequency (%)')
                ax4.grid(True, alpha=0.3)
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Visualization saved to {save_path}")
            
            plt.show()
            
        except ImportError:
            print("Matplotlib not available. Install with: pip install matplotlib seaborn")
    
    def export_results(self, years: List[int], format: str = 'json', filename: str = None):
        """
        Export results in various formats.
        
        Args:
            years: List of years to export
            format: Export format ('json', 'csv', 'txt')
            filename: Output filename (auto-generated if not provided)
        """
        if not filename:
            filename = f"christmas_sundays.{format}"
        
        if format.lower() == 'json':
            data = {
                "metadata": {
                    "generated_date": datetime.date.today().isoformat(),
                    "total_count": len(years),
                    "year_range": f"{min(years)}-{max(years)}" if years else "None"
                },
                "years": years,
                "statistics": self.statistics if self.statistics else {}
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
                
        elif format.lower() == 'csv':
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Year', 'Day of Week', 'Date'])
                for year in years:
                    date = datetime.date(year, 12, 25)
                    writer.writerow([year, calendar.day_name[date.weekday()], date.isoformat()])
                    
        elif format.lower() == 'txt':
            with open(filename, 'w') as f:
                f.write(f"Christmas Sundays ({min(years)}-{max(years)})\n")
                f.write(f"Generated: {datetime.date.today()}\n")
                f.write(f"Total: {len(years)} occurrences\n\n")
                for year in years:
                    date = datetime.date(year, 12, 25)
                    f.write(f"{year}: {calendar.day_name[date.weekday()}\n")
        
        print(f"Results exported to {filename}")

def run_tests():
    """Run comprehensive tests to verify accuracy."""
    finder = ChristmasSundayFinder()
    
    test_cases = [
        (2000, 2100, [2005, 2011, 2016, 2022, 2033, 2039, 2044, 2050, 2061, 2067, 2072, 2078, 2089, 2095]),
        (1970, 2017, [1977, 1983, 1988, 1994, 2005, 2011, 2016]),
        (2008, 2121, [2011, 2016, 2022, 2033, 2039, 2044, 2050, 2061, 2067, 2072, 2078, 2089, 2095, 2101, 2107, 2112, 2118])
    ]
    
    print("Running accuracy tests...")
    all_passed = True
    
    for start, end, expected in test_cases:
        result = finder.find_xmas_sunday_optimized(start, end)
        if result == expected:
            print(f"✓ Test {start}-{end}: PASSED")
        else:
            print(f"✗ Test {start}-{end}: FAILED")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            all_passed = False
    
    if all_passed:
        print("\n🎄 All tests passed! The implementation is 100% accurate.")
    else:
        print("\n❌ Some tests failed.")
    
    return all_passed

def main():
    """Main function with CLI interface."""
    parser = argparse.ArgumentParser(description='Find years where Christmas falls on Sunday')
    parser.add_argument('--start', type=int, default=2000, help='Start year')
    parser.add_argument('--end', type=int, default=2100, help='End year')
    parser.add_argument('--method', choices=['basic', 'calendar', 'optimized', 'generator'], 
                       default='optimized', help='Calculation method')
    parser.add_argument('--analyze', action='store_true', help='Perform detailed analysis')
    parser.add_argument('--visualize', action='store_true', help='Create visualizations')
    parser.add_argument('--export', choices=['json', 'csv', 'txt'], help='Export results')
    parser.add_argument('--test', action='store_true', help='Run accuracy tests')
    
    args = parser.parse_args()
    
    if args.test:
        run_tests()
        return
    
    finder = ChristmasSundayFinder()
    
    # Choose method
    if args.method == 'basic':
        years = finder.find_xmas_sunday_basic(args.start, args.end)
    elif args.method == 'calendar':
        years = finder.find_xmas_sunday_calendar(args.start, args.end)
    elif args.method == 'optimized':
        years = finder.find_xmas_sunday_optimized(args.start, args.end)
    elif args.method == 'generator':
        years = list(finder.find_xmas_sunday_generator(args.start, args.end))
    
    # Display results
    print(f"\n🎄 Christmas Sundays between {args.start} and {args.end}:")
    print(f"Found {len(years)} occurrences:")
    print(years)
    
    # Analysis
    if args.analyze:
        print("\n📊 Analysis:")
        analysis = finder.analyze_patterns(args.start, args.end)
        for key, value in analysis.items():
            if key != 'years_list':
                print(f"{key}: {value}")
    
    # Visualization
    if args.visualize:
        finder.visualize_data(args.start, args.end)
    
    # Export
    if args.export:
        finder.export_results(years, args.export)

if __name__ == "__main__":
    main()
